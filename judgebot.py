#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""JudgeBot.

A Slackbot that handles requests for Oracle text,
Comprehensive Rules and other such useful garbage
"""
import random, sys, difflib
import pysqlite2.dbapi2 as sqlite
from pyparsing import oneOf, OneOrMore, Combine, Word, Literal, Optional, alphanums, dblQuotedString, ParseException, ParseFatalException
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
except sqlite.OperationalError:
    logging.error("Unable to open database - goodbye")
    sys.exit(0)

# Check if the database actually has stuff
try:
    c.execute('SELECT DISTINCT(name) FROM cards')
    allCardNames = [y[0].lower() for y in c.fetchall()]
    numCards = len(allCardNames)
    logging.debug("Found %d cards" % numCards)
except sqlite.OperationalError:
    logging.error("No cards in DB? Try running dbimport.py")
    sys.exit(1)


def messagekey(message, *args, **kwargs):
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


def intersperse(delimiter, seq):
    """Intersperse a value amongst every item in a list.

    https://stackoverflow.com/questions/5655708/python-most-elegant-way-to-intersperse-a-list-with-an-element
    >>> list(intersperse(666, ["once", "upon", "a", 90, None, "time"])
    ["once", 666, "upon", 666, "a", 666, 90, 666, None, 666, "time"]
    """
    return islice(chain.from_iterable(izip(repeat(delimiter), seq)), 1, None)

rule_regexp = re.compile('!{0,1}(?:\d)+\.(?:.*)')
bot_command_regex = re.compile('!([^!|&]+)')


def validate_colon_mode(s, loc, tokens):
    """Make sure colon modes are followed by a colon."""
    if s[loc + 1] != ':':
        raise ParseFatalException(s, loc, "Mode must be followed by a colon")

colon_mode = oneOf("n o t cn in pow tou cmc r f a banned legal restricted is set").setParseAction(validate_colon_mode)
colon_or_bang_mode = "c"
math_mode = oneOf("mana pow tou cmc")
colon_operator = ":"
bang_operator = "!"
math_operator = oneOf("= >= > <= < !")
boolean_operators = oneOf("and not or")
brackets = oneOf("( )")
operand = (Word(alphanums) | dblQuotedString | OneOrMore(Combine(Literal("{") + Word(alphanums + "\\") + Literal("}"))))

colon_total = colon_mode + colon_operator
colon_or_bang_total = colon_or_bang_mode + oneOf([colon_operator, bang_operator])
math_total = math_mode + math_operator

total_thing = Combine((colon_total | colon_or_bang_total | math_total) + operand)
super_total = OneOrMore(Optional(OneOrMore(boolean_operators)) + Optional(OneOrMore(brackets)) + total_thing + Optional(OneOrMore(brackets)) + Optional(OneOrMore(boolean_operators)))


def dispatch_message(message, raw_message, channel):
    """For a message, figure out how to handle it and return the text to reply with.

    INPUT: message = Message string
    INPUT: channel = TRUE if message came from a main channel, FALSE if came from PM
    OUTPUT: (optional: list of) tuple of (reply_message, pm_override)
    OUTPUT: pm_override is TRUE if the reply should go through PM regardless

    If they give us "<string> extend", assume that it's "<cardname extend>".
    If they give us "<string>*", assume that it's "<cardname*>"
    """
    logging.debug("Dispatching message: {} (Raw text {})".format(message, raw_message))
    if message == "help":
        return (help(), True)
    elif message == "helpsearch":
        return (helpsearch(), True)
    elif message.startswith("url "):
        return (url(message[4:]), False)
    elif message.startswith("printsets"):
        c.execute('SELECT DISTINCT(name), code, releaseDate FROM sets ORDER BY ' + ('releaseDate' if message.endswith("inorder") else 'name') + ' ASC')
        message_out = ""
        for name, code, date in [(x[0], x[1], x[2]) for x in c.fetchall()]:
            message_out += name + " (" + code + ")" + " [" + date + "]" + "\n"
        return (message_out, True)
    elif message == "random":
        cards = cardSearch(c, ['en:' + random.choice(allCardNames)])
        if not cards:
            return ("No cards found :(", False)
        return (printCard(c, cards[0], quick=False, slackChannel=channel), False)
    elif message.endswith("extend"):
        cards = cardSearch(c, ['en:' + message[:-6].rstrip()])
        if not cards:
            return ("Card not found", False)
        return (printCard(c, cards[0], extend=2, quick=False), True)
    elif message.endswith("*"):
        cards = cardSearch(c, ['n:' + message[:-1]])
        if not cards:
            return ("No cards found", False)
        if len(cards) > 20:
            return ("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False)
        if channel:
            # If we've asked for some cards in a channel
            if len(cards) == 1:
                # One card is fine, show them
                return (printCard(c, cards[0], quick=False, slackChannel=channel), False)
            elif len(cards) <= 5:
                # 2 - 5 cards is fine, but only show name and mana cost
                return ("\n".join([printCard(c, card, quick=True, slackChannel=channel) for card in cards]), False)
            else:
                # > 5 is only showing name and mana cost and forced to PM
                return [("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=channel) for card in cards]), True)]
        else:
            return ("\n".join([printCard(c, card, quick=False, slackChannel=channel) for card in cards] + ["{} result/s".format(len(cards))]), False)
    elif raw_message.startswith("!s ") or raw_message.startswith("!qs "):
        logging.debug("Advanced Search!")
        quick = False
        if message == "qs":
            quick = True
            card_name = raw_message[4:].lower()
        else:
            card_name = raw_message[3:].lower()
        output = []
        try:
            parsed_data = super_total.parseString(card_name)
            logging.debug("Parsed it as: {}".format(parsed_data))
        except (ParseException, ParseFatalException) as e:
            return ("Unable to parse search terms\n{}".format(e), False)

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
            return ("No cards found", False)
        if len(cards) > 20:
            return ("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False)
        if channel:
            # If we've asked for some cards in a channel
            # If they're quick, <= 10 is fine
            if quick and len(cards) <= 10:
                return ("\n".join([printCard(c, card, quick=quick, slackChannel=channel) for card in cards]), False)
            if len(cards) <= 5:
                # 1 - 5 cards is fine
                return ("\n".join([printCard(c, card, quick=quick, slackChannel=channel) for card in cards]), False)
            else:
                # > 5 is only showing name and mana cost and forced to PM
                return [("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=channel) for card in cards]), True)]
        else:
            return ("\n".join([printCard(c, card, quick=quick, slackChannel=channel) for card in cards] + ["{} result/s".format(len(cards))]), False)
    elif raw_message.startswith("!r ") or rule_regexp.match(raw_message):
        logging.debug("Rules query!")
        if message == "r":
            message = raw_message[3:]
        return (ruleSearch(all_rules, message), False)
    else:
        logging.debug("Trying to figure out card name")
        logging.debug("Maybe we get extremely lucky")
        if message in allCardNames:
            logging.debug("We do!")
            cards = cardSearch(c, ['en:' + message])
            return (printCard(c, cards[0], quick=False, slackChannel=channel), False)
        logging.debug("We don't")
        # Handle !card1 !card2
        # Handle !card1&!card2
        # Handle Blah !card1 blah !card2
        # Don't forget if it's a PM we'll have stripped the possible initial ! so let's
        # use the raw message
        # TODO: Do it backwards, so longest matches are better
        command_list = bot_command_regex.findall(raw_message)
        logging.debug("Command list: {}".format(command_list))
        cards_found = []
        for card in command_list:
            if card in allCardNames:
                logging.debug("Bailing early due to exact match")
                cards_found.append('en:"%s"' % card)
                continue
            card_tokens = re.split(' |&', raw_message[raw_message.find(card):])
            logging.debug("Tokenising: {}".format(card_tokens))
            backup = []
            real = False
            for i in xrange(1, len(card_tokens) + 1):
                card_name = " ".join(card_tokens[:i])
                if card_tokens[i - 1].startswith("!"):
                    break
                if not backup:
                    backup.extend([x for x in allCardNames if difflib.SequenceMatcher(None, x.split(", ")[0].lower(), card_name.lower()).ratio() >= 0.8])
                real = difflib.get_close_matches(card_name, allCardNames, cutoff=0.8)
                if len(real):
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
                return ("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False)
            if len(cards) <= 5:
                return ("\n".join([printCard(c, card, quick=False, slackChannel=channel) for card in cards]), False)
            else:
                return [("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=False, slackChannel=channel) for card in cards]), True)]
        else:
            logging.debug("I didn't understand the command")
            return ("", False)


def send_user_pm(user, text="Initiating comms..."):
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
def find_pm_channel(message):
    """Find a user's private message channel."""
    for channel_id, channel in iteritems(message._client.channels):
        if channel.get('user', "") == message.body['user']:
            logging.debug("Found PM channel")
            return channel_id
    return None


@listen_to('!(\S+)')
def handle_public_message(message, message_text):
    """Listen to the channels, respond to something that looks like a command."""
    logging.debug("Received a public command.  Raw text: %s" % (message.body['text']))
    try:
        logging.debug("The channel name is #{}".format(message.channel._body['name']))
    except KeyError:
        logging.debug("Private channel ID {}".format(message.body['channel']))
    logging.debug("The regexp gives me {}".format(message_text))
    if message_text.startswith("!"):
        logging.debug("Stripping leading !")
        message_text = message_text[1:]

    replies = dispatch_message(message_text.lower().rstrip(), message.body['text'], channel=True)
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
def handle_private_message(message, message_text):
    """Receive a private message from the user and figure out how to respond."""
    logging.debug("Received private message from %s.  Raw text: %s" % (message._client.users[message.body['user']]['real_name'], message.body['text']))
    if message_text.startswith("!"):
        logging.debug("Stripping leading !")
        message_text = message_text[1:]

    replies = dispatch_message(message_text.lower().rstrip(), message.body['text'], channel=False)
    if type(replies) is not list:
        replies = [replies]
    for reply in replies:
        if reply[0]:
            message.reply(reply[0])

if __name__ == '__main__':
    try:
        logging.debug("Opening CR file")
        with open('CR.txt') as data_file:
            rules = data_file.readlines()
    except IOError:
        logging.error("Unable to open Comprehensive Rules, r search will not be available")
        rules = []

    terms = {}
    all_rules = {}
    for rule in rules:
        x = rule.split('. ')
        all_rules[x[0]] = ". ".join(x[1:])
    del rules

    numCards = -1

    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

    bot = Bot()
    logging.debug("Bot instantiated")
    bot.run()
