#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""JudgeBot.

A Slackbot that handles requests for Oracle text,
Comprehensive Rules and other such useful garbage
"""
import random, sys, difflib
import pysqlite2.dbapi2 as sqlite
from pyparsing import oneOf, OneOrMore, Combine, Word, Literal, Optional, alphanums, dblQuotedString, sglQuotedString, ParseException, ParseFatalException
from frytherer import cardSearch, printCard, ruleSearch, help, helpsearch, url
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

import logging
logging.basicConfig(level=logging.DEBUG)

cache = LRUCache(maxsize=100)
lock = RLock()
logging.debug("Cache instantiated")

# Try open the database
logging.debug("Opening database connection")
try:
    conn = sqlite.connect('frytherer.db', check_same_thread=False)
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    conn.row_factory = sqlite.Row
    c = conn.cursor()
except sqlite.OperationalError:  # pragma: no cover
    logging.error("Unable to open database - goodbye")
    sys.exit(0)

# Check if the database actually has stuff
try:
    c.execute('SELECT DISTINCT(name) FROM cards ORDER BY name')
    allCardNames = [y[0].lower() for y in c.fetchall()]
    numCards = len(allCardNames)
    logging.debug("Found %d cards" % numCards)
except sqlite.OperationalError:  # pragma: no cover
    logging.error("No cards in DB? Try running dbimport.py")
    sys.exit(1)

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
    x = rule.split('. ')
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

rule_regexp = re.compile('!{0,1}(?:\d)+\.(?:.*)')
bot_command_regex = re.compile('!([^!|&]+)')
single_quoted_word = re.compile('^(?:\"|\')\w+(?:\"|\')$')


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


def dispatch_message(incomingMessage, fromChannel):
    """For a message, figure out how to handle it and return the text to reply with.
    The message should probably start with a "!" or at least individual commands within it should.

    INPUT: incomingMessage = Message string
    INPUT: fromChannel = TRUE if message came from a main channel, FALSE if came from PM
    OUTPUT: List of tuple of (reply_message, pm_override)
    OUTPUT: pm_override is TRUE if the reply should go through PM regardless
    """
    logging.debug("Dispatching message: {}".format(incomingMessage))
    command_list = bot_command_regex.findall(incomingMessage)
    logging.debug("Command list: {}".format(command_list))
    ret = []
    for message in command_list:
        message = message.rstrip()
        if re.match(single_quoted_word, message):
            logging.debug("Single quoted word detected, stripping")
            message = message[1:-1]
        message_words = message.split(" ")
        if message == "help" or message_words[0] == "help":
            ret.append((help(), True))
        elif message == "helpsearch" or message_words[0] == "helpsearch":
            ret.append((helpsearch(), True))
        elif message in ["alldocs", "mt", "missed trigger", "l@ec", "looking at extra cards", "hce", "hidden card error", "mpe", "mulligan procedure error", "grv", "game rule violation", "ftmgs", "failure to maintain game state", "tardiness", "oa", "outside assistance", "slow play", "insufficient shuffling", "ddlp", "deck/decklist problem", "lpv", "limited procedure violation", "cpv", "communication policy violation", "mc", "marked cards", "usc minor", "usc major", "idaw", "improperly determining a winner", "bribery", "ab", "aggressive behaviour", "totm", "theft of tournament material", "stalling", "cheating"] or message.startswith("alldocs ") or message[0:4] in ["url ", "mtr ", "ipg ", "mtr", "ipg", "amtr", "aipg", "jar", "jar ", "peip", "pptq", "rptq"]:
            ret.append((url(message), False))
        elif message.startswith("printsets"):
            c.execute('SELECT DISTINCT(name), code, releaseDate FROM sets ORDER BY ' + ('releaseDate' if message.endswith("inorder") else 'name') + ' ASC')
            message_out = ""
            for name, code, date in [(x[0], x[1], x[2]) for x in c.fetchall()]:
                message_out += name + " (" + code + ")" + " [" + date + "]" + "\n"
            ret.append((message_out, True))
        elif message == "random":
            cards = cardSearch(c, ['en:' + random.choice(allCardNames)])
            if not cards:
                return ("No cards found :(", False)
            ret.append((printCard(c, cards[0], quick=False, slackChannel=fromChannel), False))
        elif message.endswith("extend"):
            cards = cardSearch(c, ['en:' + message[:-6].rstrip()])
            if not cards:
                return ("", False)
            ret.append((printCard(c, cards[0], extend=2, quick=False), True))
        elif message.endswith("*"):
            cards = cardSearch(c, ['n:' + message[:-1]])
            if not cards:
                ret.append(("", False))
            if len(cards) > 20:
                ret.append(("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False))
            if fromChannel:
                # If we've asked for some cards in a channel
                if len(cards) == 1:
                    # One card is fine, show them
                    ret.append((printCard(c, cards[0], quick=False, slackChannel=fromChannel), False))
                elif len(cards) <= 5:
                    # 2 - 5 cards is fine, but only show name and mana cost
                    ret.append(("\n".join([printCard(c, card, quick=True, slackChannel=fromChannel) for card in cards]), False))
                else:
                    # > 5 is only showing name and mana cost and forced to PM
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
                ret.append(("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False))
            if fromChannel:
                # If we've asked for some cards in a channel
                # If they're quick, <= 10 is fine
                if quick and len(cards) <= 10:
                    ret.append(("\n".join([printCard(c, card, quick=quick, slackChannel=fromChannel) for card in cards]), False))
                if len(cards) <= 5:
                    # 1 - 5 cards is fine
                    ret.append(("\n".join([printCard(c, card, quick=quick, slackChannel=fromChannel) for card in cards]), False))
                else:
                    # > 5 is only showing name and mana cost and forced to PM
                    ret.extend([("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=fromChannel) for card in cards]), True)])
            else:
                ret.append(("\n".join([printCard(c, card, quick=quick, slackChannel=fromChannel) for card in cards] + ["{} result/s".format(len(cards))]), False))
        elif message.startswith("r ") or rule_regexp.match(message):
            logging.debug("Rules query!")
            if message.startswith("r "):
                message = message[2:]
            ret.append((ruleSearch(all_rules, message), False))
        else:
            logging.debug("Trying to figure out card name")
            logging.debug("Maybe we get extremely lucky")
            if message in allCardNames:
                logging.debug("We do!")
                cards = cardSearch(c, ['en:' + message])
                ret.append((printCard(c, cards[0], quick=False, slackChannel=fromChannel), False))
                continue
            logging.debug("We don't")

            # TODO: Do it backwards, so longest matches are better
            # command_list = bot_command_regex.findall(message)
            # logging.debug("Command list: {}".format(command_list))
            cards_found = []
            # for card in command_list:
            #     if card in allCardNames:
            #         logging.debug("Bailing early due to exact match")
            #         cards_found.append('en:"%s"' % card)
            #         continue
            card_tokens = re.split(' |&', message)
            logging.debug("Tokenising: {}".format(card_tokens))
            backup = []
            real = False
            for i in xrange(len(card_tokens), 0, -1):
                card_name = " ".join(card_tokens[:i])
                print card_name
                if card_tokens[i - 1].startswith("!"):
                    break
                if not backup:
                    #backup.extend([x for x in allCardNames if difflib.SequenceMatcher(None, x.split(", ")[0].lower(), card_name.lower()).ratio() >= 0.8])
                    print backup
                #real = difflib.get_close_matches(card_name, allCardNames, cutoff=0.8)
                real = process.extractOne(card_name, allCardNames, scorer=fuzz.ratio)
                print real
                if real[1] >= 80:
                    cards_found.append('en:"%s"' % real[0])
                    real = True
                    break
            if not real:
                if backup:
                    cards_found.append('en:"%s"' % backup[0])
            logging.debug("Finally, the cards: {}".format(cards_found))
            if cards_found:
                terms = list(intersperse("OR", cards_found))
                logging.debug("Searching for {}".format(terms))
                cards = cardSearch(c, terms)
                logging.debug("Found {} cards".format(len(cards)))
                if len(cards) > 20:
                    ret.append(("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False))
                if len(cards) <= 5 or not fromChannel:
                    ret.append(("\n".join([printCard(c, card, quick=False, slackChannel=fromChannel) for card in cards]), False))
                else:
                    ret.extend([("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=False, slackChannel=fromChannel) for card in cards]), True)])
            else:
                logging.debug("I didn't understand the command")
                ret.append(("", False))
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

    replies = dispatch_message((message.body['text']).lower().rstrip(), fromChannel=True)
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
    if not message_text.startswith("!"):
        logging.debug("Adding leading !")
        message.body['text'] = "!" + message.body['text']

    replies = dispatch_message(message.body['text'].lower().rstrip(), fromChannel=False)
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
