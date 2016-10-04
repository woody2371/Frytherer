#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""JudgeBot.

A Slackbot that handles requests for Oracle text,
Comprehensive Rules and other such useful garbage
"""
import random, sys, string, ast
import pysqlite2.dbapi2 as sqlite
from pyparsing import oneOf, OneOrMore, Combine, Word, Literal, Optional, alphanums, dblQuotedString, sglQuotedString, ParseException, ParseFatalException
from frytherer import cardSearch, printCard, ruleSearch, help, helpsearch, url, dedupe, cardExtendSearch
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from six import iteritems
import requests
try:
    import re2 as re
except ImportError:
    import re
from itertools import chain, izip, repeat, islice
from threading import RLock
from cachetools import cached, LRUCache, hashkey
from fuzzywuzzy import process, fuzz
from HTMLParser import HTMLParser

import logging
logging.basicConfig(level=logging.DEBUG)

cache = LRUCache(maxsize=100)
lock = RLock()
logging.debug("Cache instantiated")
h = HTMLParser()

# Try open the database
logging.debug("Opening database connection")
try:
    conn = sqlite.connect('frytherer.db', flags=sqlite.SQLITE_OPEN_READONLY, check_same_thread=False)
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    conn.row_factory = sqlite.Row
    c = conn.cursor()
except sqlite.OperationalError:  # pragma: no cover
    logging.error("Unable to open database - goodbye")
    sys.exit(0)

# Check if the database actually has stuff
try:
    c.execute('SELECT DISTINCT(name) FROM cards WHERE layout NOT IN ("token", "vanguard", "plane", "phenomenon", "scheme") AND NOT(printings = "[u\'UGL\']" or printings = "[u\'UNH\']") ORDER BY type, name')
    allCardNames = [y[0].lower() for y in c.fetchall()]
    numCards = len(allCardNames)
    logging.debug("Found %d cards" % numCards)
except sqlite.OperationalError:  # pragma: no cover
    logging.error("No cards in DB? Try running dbimport.py")
    sys.exit(1)

c.execute('SELECT DISTINCT(name) FROM cards WHERE type LIKE ? OR type LIKE ? order by type', ('%Legendary%', '%Planeswalker%'))
allLegendaries = [y[0].lower() for y in c.fetchall()]

try:
    logging.debug("Opening CR file")
    with open('CR.txt') as data_file:
        rules = data_file.readlines()
except IOError:  # pragma: no cover
    logging.error("Unable to open Comprehensive Rules, r search will not be available")
    rules = []

terms = {}
all_rules = {}
for rule in rules:
    x = re.split(r'(?:\. )|(?:: )', rule)
    all_rules[x[0]] = ". ".join(x[1:])
del rules


def messagekey(message, *args, **kwargs):   # pragma: no cover
    """Custom hashing function for LRU Cache."""
    key = hashkey(*args, **kwargs)
    key += (message.body['user'],)
    return key

# TODO: PPTQ Stuff
# Legalities in card output
# !Rulings & !flavour & !reminder etc
# Better fuzzy matching
# Test suite (for regressions)
# Match all our commands inside a message D:
# Don't retrieve a billion cards only to tell the user that it's too many to show. Do a COUNT() first
# n:One Two Three should probably be handled as n:"One Two Three"
# Foreign search
# Rules parsing to include examples
# Rule search to return multiple possible rules


def intersperse(delimiter, seq):  # pragma: no cover
    """Intersperse a value amongst every item in a list.

    https://stackoverflow.com/questions/5655708/python-most-elegant-way-to-intersperse-a-list-with-an-element
    >>> list(intersperse(666, ["once", "upon", "a", 90, None, "time"])
    ["once", 666, "upon", 666, "a", 666, 90, 666, None, 666, "time"]
    """
    return islice(chain.from_iterable(izip(repeat(delimiter), seq)), 1, None)

rule_regexp = re.compile(r'((?:\d)+\.(?:.*?)\S*)')
bot_command_regex = re.compile(r'[!&]([^!&]+)')
single_quoted_word = re.compile(r'^(?:\"|\')\w+(?:\"|\')$')
split_card_regex = re.compile(r'(.*?)\s*//\s*(.*)')
non_text_regex = re.compile(r'^[^\w]+$')
#word_ending_in_bang = re.compile(r'\w+! ')
#word_starting_with_bang = re.compile(r'[^\w]!(?: *)\w+')
word_ending_in_bang = re.compile(r'\S+! ')
word_starting_with_bang = re.compile(r'\s+!(?: *)\S+')
gathererRuling_regex = re.compile(r'^(?:(?P<start_number>\d+) (?P<name>.+)|(?P<name2>.*?) ?(?P<end_number>\d+).*?|(?P<name3>.+))')


def validate_colon_mode(s, loc, tokens):
    """Make sure colon modes are followed by a colon."""
    # logging.debug("S: {} Loc: {} Toks: {} S[LOC]: {} S[LOC+1]: {}".format(s, loc, tokens, s[loc], s[loc+1]))
    if s[loc + len(tokens[0])] != ':':
        raise ParseFatalException(s, loc, "Mode must be followed by a colon")

colon_mode = oneOf("n en o t cn in pow tou cmc r f a banned legal restricted is set").setParseAction(validate_colon_mode)
colon_or_bang_mode = "c"
math_mode = oneOf("mana pow tou cmc")
colon_operator = ":"
bang_operator = "!"
math_operator = oneOf("= >= > <= < !")
boolean_operators = oneOf("and not or")
brackets = oneOf("( )")
operand = (Word(alphanums) | dblQuotedString | sglQuotedString | OneOrMore(Combine(Literal("{") + Word(alphanums + "\\") + Literal("}"))))

colon_total = colon_mode + colon_operator
colon_or_bang_total = colon_or_bang_mode + oneOf([colon_operator, bang_operator])
math_total = math_mode + math_operator

total_thing = Combine((colon_total | colon_or_bang_total | math_total) + operand)
super_total = OneOrMore(Optional(OneOrMore(boolean_operators)) + Optional(OneOrMore(brackets)) + total_thing + Optional(OneOrMore(brackets)) + Optional(OneOrMore(boolean_operators)))


def guessCardName(message, card_tokens):
    # TODO: Be better with the [f(x) for x if f(x)] efficiency
    logging.debug("Guessing! {}".format(card_tokens))
    cards_found = []
    for i in xrange(len(card_tokens), 0, -1):
        card_name = " ".join(card_tokens[:i])
        if re.match(single_quoted_word, card_name):
            logging.debug("Single quoted word detected, stripping")
            card_name = card_name[1:-1]
        # Strip ending punctuation etc
        card_name = re.sub(r'\W$', '', card_name)
        logging.debug("Processing {}".format(card_name))
        logging.debug("Trying to figure out card name")
        logging.debug("Maybe we get extremely lucky")
        if card_name in allCardNames:
            logging.debug("We do!")
            cards_found.append('en:' + card_name)
            break
        logging.debug("We don't")
        if len(card_name) < 3:
            logging.warning("Skipping due to being too short")
            continue
        if card_tokens[i - 1].startswith("!"):
            logging.error("Exiting due to new command")
            break
        if card_name == "thank you":
            continue
        # print process.extractOne(card_name, allCardNames, scorer=fuzz.ratio)
        # print process.extractOne(card_name, allCardNames, scorer=fuzz.partial_ratio)
        # print process.extractOne(card_name, allCardNames, scorer=fuzz.token_sort_ratio)
        # print process.extractOne(card_name, allCardNames, scorer=fuzz.token_set_ratio)
        # print "---"
        # print process.extractOne(card_name, allLegendaries, scorer=fuzz.ratio)
        # print process.extractOne(card_name, allLegendaries, scorer=fuzz.partial_ratio)
        # print process.extractOne(card_name, allLegendaries, scorer=fuzz.token_sort_ratio)
        # print process.extractOne(card_name, allLegendaries, scorer=fuzz.token_set_ratio)

        # Get best normal guess
        extracted_cards = process.extract(card_name, allCardNames, scorer=fuzz.ratio)
        logging.debug("Candidates: {}".format(extracted_cards))
        (quick_guess_card, quick_guess_ratio) = extracted_cards[0]
        quick_guess_card = quick_guess_card.encode('utf-8')
        logging.debug("Best guess: {} ({})".format(quick_guess_card, quick_guess_ratio))

        if quick_guess_ratio > 85 and quick_guess_card in card_name and len(quick_guess_card) > 5:
            # 85% for borborygmos, en
            # Does our input appear entirely in our guess?
            logging.error("Early Exit Fry Style")
            cards_found.append('en:"{}"'.format(quick_guess_card))
            break
        if quick_guess_ratio >= 75 and card_name in quick_guess_card and len(quick_guess_card) > 5 and card_name != "goblin":
            # 75% for Take Poss vs Take Possession (was 90)
            # Does our guess appear entirely in our input?
            logging.error("Early Exit Woody Style")
            cards_found.append('en:"{}"'.format(quick_guess_card))
            break
        prefix_check = [c for c in allCardNames if c.startswith(card_name)]
        if len(prefix_check) == 1:
            logging.error("Prefix Check!")
            cards_found.append('en:"{}"'.format(prefix_check[0]))
            break
        elif len(prefix_check) >= 5:
            logging.error("Too many prefixes!")
            return ["en:" + c for c in prefix_check]
        if type(card_name) is unicode:
            card_name_no_punctuation = card_name.translate({ord(c): None for c in string.punctuation})
        else:
            card_name_no_punctuation = card_name.translate(string.maketrans("", ""), string.punctuation)
        prefix_check_2 = [c for c in allCardNames if c.startswith(card_name_no_punctuation)]
        if len(prefix_check_2) == 1:
            logging.error("Prefix Check No Punctuation!")
            cards_found.append('en:"{}"'.format(prefix_check_2[0]))
            break
        listOfCardsToCheck = (prefix_check + prefix_check_2) or allCardNames
        if len(card_tokens) == 1 or len(card_tokens) == 2:
            # Check thee legendaries
            legends = process.extract(card_name, allLegendaries, scorer=fuzz.token_set_ratio)
            starting_legends = filter(lambda x: x[0].startswith(card_name), legends)
            if len(starting_legends) == 1 and starting_legends[0][1] == 100:
                logging.error("Legendary YOLO")
                cards_found.append('en:"{}"'.format(starting_legends[0][0]))
                break
        if len(card_name) >= 4 and quick_guess_ratio > 64 and fuzz.partial_ratio(card_name, quick_guess_card) == 100:
            # 64% for "valakut"
            logging.error("Good enough for Government work")
            cards_found.append('en:"{}"'.format(quick_guess_card))
            break
        if quick_guess_ratio >= 80:
            # First pass is probably pretty good
            # Kind of have to keep it at 81
            v2 = process.extractOne(card_name, allCardNames, scorer=fuzz.partial_ratio)
            v4 = process.extractOne(card_name, allCardNames, scorer=fuzz.token_set_ratio)

            logging.debug("Attempted Mulligan into {} {}".format(v2, v4))
            if v2[1] >= 80 and v4[1] >= 80:
                # Does our input appear entirely in our better guesses?
                if card_name.replace(" ", "") in v2[0].replace(" ", ""):
                    logging.error("Poop")
                    cards_found.append('en:"{}"'.format(v2[0]))
                    break
                elif card_name.replace(" ", "") in v4[0].replace(" ", ""):
                    logging.error("Poop2")
                    cards_found.append('en:"{}"'.format(v4[0]))
                    break
            if v2[0] != quick_guess_card and v2[0] == v4[0] and v2[1] > quick_guess_ratio and len(v2[0]) > len(quick_guess_card):
                cards_found.append('en:"{}"'.format(v2[0]))
                logging.warning("Mulligan success!")
                break
            elif v2[0] == quick_guess_card and v4[0] == quick_guess_card:
                vx = [(x, fuzz.token_sort_ratio(x[:len(card_name)], card_name)) for x in allCardNames if (fuzz.token_sort_ratio(x[:len(card_name)], card_name) > 95)]
                if vx and vx[0][0] != v2[0]:
                    cards_found.append('en:"{}"'.format(vx[0][0]))
                    logging.warning("WILD CARD BITCHES!")
                else:
                    logging.warning("Mulligan override!")
                    cards_found.append('en:"{}"'.format(quick_guess_card))
                break
            else:
                logging.debug("Outer Else")
                # Try the best partial card match
                backupCard = [(x, fuzz.ratio(x[:len(card_name)], card_name)) for x in allCardNames if (fuzz.ratio(x[:len(card_name)], card_name) > quick_guess_ratio + 10)]
                if backupCard:
                    best = max(backupCard, key=lambda x: x[1])
                    logging.debug("Backing up with {}".format(best))
                    if (len(best[0]) >= len(quick_guess_card)):
                        logging.warning("It's good!")
                        cards_found.append('en:"%s"' % best[0])
                        break
                else:
                    logging.debug("Inner Else")
                    if quick_guess_ratio < 87:
                        # Last chance qualifiers
                        (best, score) = process.extractOne(card_name, allCardNames, scorer=fuzz.token_sort_ratio)
                        if score == 100 and len(best) >= len(quick_guess_card):
                            logging.warning("Extra special backup: {}".format(best))
                            cards_found.append('en:"%s"' % best)
                            break
                        elif card_tokens[-1] == "and":
                            logging.error("Do or Die")
                            continue
                        else:
                            logging.debug("Screw it")
                            cards_found.append('en:"{}"'.format(quick_guess_card))
                            break
                    else:
                        logging.debug("Deepest Else")
                        cards_found.append('en:"{}"'.format(quick_guess_card))
                        break
        elif quick_guess_ratio >= 60:
            v2 = process.extractOne(card_name, allLegendaries, scorer=fuzz.partial_ratio)
            if v2[1] >= 90 and v2[0] == quick_guess_card:
                logging.warning("Wat")
                cards_found.append('en:"{}"'.format(quick_guess_card))
                break
    # We tried all the words down to one and no matches. Try a bunch of bullshit
    if not cards_found and len(message) >= 4:
        logging.debug("Commence backup")
        l = [message]
        if len(card_tokens) > 1:
            l.append(card_tokens[0])
        for backup_card_name in l:
            if len(backup_card_name) < 4:
                continue
            logging.debug("Looping through {}".format(backup_card_name))
            if len(backup_card_name) >= 4:
                backup1 = process.extract(backup_card_name, allLegendaries, scorer=fuzz.token_set_ratio)
                backup2 = [x for x in allCardNames if x.startswith(backup_card_name)]
                backup3 = [x for x in allCardNames if fuzz.ratio(x[:len(backup_card_name)], backup_card_name) >= 85]  # Was >87
                logging.debug("FOUND BACKUP1: {} BACKUP2: {} BACKUP3: {}".format(backup1, backup2, backup3))
                if len(backup3) == 1:
                    logging.warning("Using Backup 3")
                    cards_found.append('en:"%s"' % backup3[0])
                    break
                elif len(backup2) == 1:
                    logging.warning("Using exact Backup 2")
                    cards_found.append('en:"%s"' % backup2[0])
                    break
                elif backup1:
                    # Try match from the start
                    foundMax = 0
                    foundMaxRatio = 0
                    foundMaxName = ""
                    for b1 in backup1:
                        if b1[1] >= 85 and b1[1] >= foundMax:
                            foundMax = b1[1]
                            r = fuzz.ratio(b1[0][:len(backup_card_name)], backup_card_name)
                            if r > foundMaxRatio:
                                foundMaxRatio = r
                                foundMaxName = b1[0]
                    if foundMax:
                        logging.warning("Using Backup 1")
                        cards_found.append('en:"%s"' % foundMaxName)
                        break
                if backup2:
                    logging.debug("Trying Dodgy Backup 2")
                    # ultimate last resort, pick the option with the comma
                    v = filter(lambda x: ',' in x, backup2)
                    if len(v) == 1:
                        logging.warning("ULR")
                        cards_found.append('en:"%s"' % v[0])
                        break
                    else:
                        # super mega ultimate last resort, pick the longest one :D
                        logging.warning("SMULR")
                        cards_found.append('en:"%s"' % max(backup2, key=len))
                        break
                    logging.debug("Nope")

    logging.debug("Finally, the cards: {}".format(cards_found))
    return cards_found

def dispatch_message(incomingMessage, fromChannel):
    """For a message, figure out how to handle it and return the text to reply with.
    The message should probably start with a "!" or at least individual commands within it should.

    INPUT: incomingMessage = Message string
    INPUT: fromChannel = TRUE if message came from a main channel, FALSE if came from PM
    OUTPUT: List of tuple of (reply_message, pm_override)
    OUTPUT: pm_override is TRUE if the reply should go through PM regardless
    """
    incomingMessage = h.unescape(incomingMessage)
    logging.debug("Dispatching message: {} (Channel: {})".format(incomingMessage, fromChannel))
    if word_ending_in_bang.search(incomingMessage) and not word_starting_with_bang.search(incomingMessage):
        logging.warning("WEIB Skip")
        return []
    if "!!" in incomingMessage:
        logging.warning("Double Bang Skip")
        return []
    command_list = bot_command_regex.findall(incomingMessage)
    logging.debug("Command list: {}".format(command_list))
    ret = []
    for (idx, message) in enumerate(command_list):
        if non_text_regex.match(message) or message.startswith("  "):
            logging.warning("Iffy skip")
            continue
        message = message.strip()
        if re.match(single_quoted_word, message):
            logging.debug("Single quoted word detected, stripping")
            message = message[1:-1]
        if message == '':
            continue
        if message.startswith("card "):
            message = message[5:]

        rem = rule_regexp.match(message)
        if split_card_regex.match(message):
            # Process the left word, slip the right one into the command list
            (left, right) = split_card_regex.match(message).groups()
            if "http" not in left:
                logging.warning("Split card detected! {} // {}".format(left, right))
                message = left
                command_list.insert(idx + 1, right)
            else:
                pass

        card_tokens = re.split(' ', message[0:35])
        card_tokens = filter(lambda x: x != '', card_tokens)
        logging.debug("Tokenising: {}".format(card_tokens))
        message_words = message.split()

        if message == "help" or message_words[0] == "help":
            ret.append((help(), True))
        elif message_words[0] == "helpsearch":
            ret.append((helpsearch(), True))
        elif message in ["alldocs", "mt", "missed trigger", "l@ec", "looking at extra cards", "hce", "hidden card error", "mpe", "mulligan procedure error", "grv", "game rule violation", "ftmgs", "failure to maintain game state", "tardiness", "oa", "outside assistance", "slow play", "insufficient shuffling", "ddlp", "deck/decklist problem", "lpv", "limited procedure violation", "cpv", "communication policy violation", "mc", "marked cards", "usc minor", "usc major", "idaw", "improperly determining a winner", "bribery", "ab", "aggressive behaviour", "totm", "theft of tournament material", "stalling", "cheating"] or message.startswith("alldocs ") or message[0:4] in ["url ", "mtr ", "ipg ", "mtr", "ipg", "amtr", "aipg", "jar", "jar ", "peip", "pptq", "rptq"]:
            ret.append((url(message), False))
        elif message.startswith("printsets"):
            c.execute('SELECT DISTINCT(name), code, releaseDate FROM sets ORDER BY ' + ('releaseDate' if message.endswith("inorder") else 'name') + ' ASC')
            message_out = ""
            for name, code, date in [(x[0], x[1], x[2]) for x in c.fetchall()]:
                message_out += name + " (" + code + ")" + " [" + date + "]" + "\n"
            ret.append((message_out, True))
        elif message_words[0] == "random":
            cards = cardSearch(c, ['en:' + random.choice(allCardNames)])
            if not cards:
                return ("No cards found :(", False)
            ret.append((printCard(c, cards[0], quick=False, slackChannel=fromChannel), False))
        elif len(message_words) > 1 and message_words[1] == "extend":
            cards = cardSearch(c, ['en:' + message[:-6].rstrip()])
            if not cards:
                return ("", False)
            ret.append((printCard(c, cards[0], extend=2, quick=False), True))
        elif message_words[0].endswith("*") or message.endswith("*"):
            if message_words[0].endswith("*"):
                message = message_words[0]
            cards = cardSearch(c, ['n:' + message[:-1]])
            if not cards:
                ret.append(("", False))
            if len(cards) > 20:
                ret.append(("Too many cards to print! ({} > 20).".format(len(cards)), False))
            if fromChannel:
                # If we've asked for some cards in a channel
                if len(cards) == 1:
                    # One card is fine, show them
                    ret.append((printCard(c, cards[0], quick=False, slackChannel=fromChannel), False))
                elif len(cards) <= 5:
                    # 2 - 5 cards is fine, but only show name and mana cost
                    ret.append(("\n".join([printCard(c, card, quick=True, slackChannel=fromChannel) for card in cards]), False))
                elif len(cards) <= 30:
                    # > 5 <= 30 is only showing name and mana cost and forced to PM
                    ret.extend([("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=fromChannel) for card in cards]), True)])
            else:
                ret.append(("\n".join([printCard(c, card, quick=False, slackChannel=fromChannel) for card in cards] + ["{} result/s".format(len(cards))]), False))
        elif message.startswith("s ") or message.startswith("qs "):
            logging.debug("Advanced Search!")
            quick = False
            if message.startswith("qs"):
                quick = True
                card_name = message[3:].lower()
            else:
                card_name = message[2:].lower()
            logging.debug("Searching for {}".format(card_name))
            output = []
            try:
                parsed_data = super_total.parseString(card_name)
                logging.debug("Parsed it as: {}".format(parsed_data))
            except (ParseException, ParseFatalException) as e:
                ret.append(("Unable to parse search terms\n{}".format(e), False))
                continue

            last_was_s = False
            for idx, x in enumerate(parsed_data.asList()):
                if x in ["and", "or", "not"]:
                    output.append(x)
                    last_was_s = False
                elif x == "(":
                    if last_was_s:
                        output.append("AND")
                    output.append("(")
                    last_was_s = False
                elif x == ")":
                    output.append(")")
                    last_was_s = False
                else:
                    if last_was_s:
                        output.append("AND")
                    output.append(x)
                    last_was_s = True
            logging.debug("Advanced search final terms: {}".format(output))
            cards = cardSearch(c, output)
            if not cards:
                ret.append(("No cards found", False))
            if len(cards) > 20:
                ret.append(("Too many cards to print! ({} > 20).".format(len(cards)), False))
            if fromChannel:
                # If we've asked for some cards in a channel
                # If they're quick, <= 10 is fine
                if quick and len(cards) <= 10:
                    ret.append(("\n".join([printCard(c, card, quick=quick, slackChannel=fromChannel) for card in cards]), False))
                if len(cards) <= 5:
                    # 1 - 5 cards is fine
                    ret.append(("\n".join([printCard(c, card, quick=quick, slackChannel=fromChannel) for card in cards]), False))
                elif len(cards) <= 30:
                    # > 5 <= 30 is only showing name and mana cost and forced to PM
                    ret.extend([("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=fromChannel) for card in cards]), True)])
            else:
                ret.append(("\n".join([printCard(c, card, quick=quick, slackChannel=fromChannel) for card in cards] + ["{} result/s".format(len(cards))]), False))
        elif message.startswith(("r ","cr ","rule ","def ","define ")) or rem:
            logging.debug("Rules query!")
            if rem:
                message = rem.group(1)
            message = message.split(' ', 1)[1] #Strip out the command
            rs = ruleSearch(all_rules, message)
            if type(rs) is not list:
                rs = [rs]
            for r in rs:
                ret.append((r, False))
        elif message.startswith(("flavour ", "flavor ", "ruling ", "rulings ")):
            # Use regex to put all the parts of the message in accessible parts
            command = card_tokens[0]
            logging.debug(command + " text!")
            matches = gathererRuling_regex.match(message.split(' ', 1)[1])
            if matches:
                matches = matches.groupdict()
            else:
                logging.debug("No matches, that's strange.") #We should be matching everything
                continue
            matches["name"] = matches.get("name") or matches.get("name2") or matches.get("name3")  #Set our final name
            if command.startswith("ruling"):  # Check if it's a ruling, if not why do we need numbers?
                matches["num"] = matches.get("start_number") or matches.get("end_number")  #Set our ruling number
            if matches["num"] != None:
                matches["num"] = int(matches["num"])-1  # Because normal people don't think like CS people
            # Check if we matched anything
            logging.debug("Valid {} command detected".format(command))
            logging.debug("Found name {} and ruling number {}".format(matches["name"], matches["num"]))
            card_tokens = matches['name'].split(' ')
            cards_found = guessCardName(matches['name'], card_tokens)
            if len(cards_found) == 1:  # Check if we found one thing
                logging.debug("Searching for {}".format(cards_found))
                # Grab card from SQL
                cards = cardSearch(c, cards_foudn)
                # I just use the first result, people have to be exact
                # Rest of this is done in a function in frytherer.py, 
                ret = cardExtendSearch(matches, command, ret, cards[0])
            else:  #Either we found 0 or more than one cards
                logging.debug("Found {} cards, returning error".format(len(cards_found)))
                ret.append(("I found {} cards. Please type exact names.".format(len(cards_found)), False))
                continue
        else:
            cards_found = guessCardName(message, card_tokens)
            if cards_found:
                terms = list(intersperse("OR", cards_found))
                logging.debug("Searching for {}".format(terms))
                cards = cardSearch(c, terms)
                logging.debug("Found {} cards".format(len(cards)))
                if len(cards) > 20:
                    ret.append(("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False))
                if len(cards) <= 2 or not fromChannel:
                    ret.append(("\n".join([printCard(c, card, quick=False, slackChannel=fromChannel) for card in cards]), False))
                else:
                    ret.extend([("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=False, slackChannel=fromChannel) for card in cards]), True)])
            else:
                logging.debug("I didn't understand the command")
                ret.append(("", False))
    ret = dedupe(ret)
    logging.debug("--- Done ---")
    logging.debug(ret)
    return ret


def send_user_pm(user, text="Initiating comms..."):  # pragma: no cover
    """Send the specified user the specified message privately.

    Note, if the private message channel didn't already exist,
    this will create it.
    INPUT: Message object, (optional) text to send
    OUTPUT: The channel name of the user
    """
    global bot
    user_pm_channel = None
    payload = {'token': bot._client.token,
               'channel': user,
               'text': text,
               'username': 'judgebot',
               'as_user': 'true',
               }
    r = requests.get('https://slack.com/api/chat.postMessage', params=payload)
    logging.debug("Direct comms: {}".format(r.text))
    try:
        rj = r.json()
        user_pm_channel = rj['channel']
    except:
        logging.error("Error parsing json")
        logging.error(sys.exc_info())
    return user_pm_channel


@cached(cache, key=messagekey, lock=lock)
def find_pm_channel(message):  # pragma: no cover
    """Find a user's private message channel."""
    for channel_id, channel in iteritems(message._client.channels):
        if channel.get('user', "") == message.body['user']:
            logging.debug("Found PM channel")
            return channel_id
    return None


@listen_to('!(\w+)')
def handle_public_message(message, message_text):  # pragma: no cover
    """Listen to the channels, respond to something that looks like a command."""
    logging.debug("Received a public command from {}.  Raw text: {}".format(message._client.users[message.body['user']]['real_name'], message.body['text']))
    try:
        logging.debug("The channel name is #{}".format(message.channel._body['name']))
    except KeyError:
        logging.debug("Private channel ID {}".format(message.body['channel']))

    replies = dispatch_message((message.body['text']).lower().rstrip().replace("’", "'"), fromChannel=True)
    if type(replies) is not list:
        replies = [replies]
    for reply in replies:
        if not reply[0]:
            continue
        if reply[1]:
            # Force a PM
            user_pm_channel = None
            logging.debug("Attempting to find preliminary PM channel")
            user_pm_channel = find_pm_channel(message)
            if not user_pm_channel:
                logging.debug("Didn't find it, initiating comms")
                user_pm_channel = send_user_pm(message.body['user'])
            if not user_pm_channel:
                logging.debug("STILL didn't find it, guess we send directly")
                send_user_pm(message.body['user'], reply[0])
            else:
                logging.debug("Sweet, setting channel")
                logging.debug(cache)
                message.body['channel'] = user_pm_channel
        message.reply(reply[0])


@respond_to('(.*)')
def handle_private_message(message, message_text):  # pragma: no cover
    """Receive a private message from the user and figure out how to respond."""
    logging.debug("Received private message from %s.  Raw text: %s" % (message._client.users[message.body['user']]['real_name'], message.body['text']))
    if "!" not in message_text:
        logging.debug("Adding leading !")
        message.body['text'] = "!" + message.body['text']

    replies = dispatch_message(message.body['text'].lower().rstrip().replace("’", "'"), fromChannel=False)
    if type(replies) is not list:
        replies = [replies]
    for reply in replies:
        if reply[0]:
            message.reply(reply[0])

if __name__ == '__main__':   # pragma: no cover
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

    bot = Bot()
    logging.debug("Bot instantiated")
    bot.run()
