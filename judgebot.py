#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""JudgeBot.

A Slackbot that handles requests for Oracle text,
Comprehensive Rules and other such useful garbage
"""
import random, sys, difflib
import pysqlite2.dbapi2 as sqlite
from pyparsing import oneOf, OneOrMore, Combine, Word, Literal, Optional, alphanums, dblQuotedString, ParseException, ParseFatalException
from frytherer import gathererCapitalise, cardSearch, printCard, ruleSearch, help, helpsearch, url
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from six import iteritems
import requests
try:
    import re2 as re
except ImportError:
    import re

import logging
logging.basicConfig(level=logging.DEBUG)

# TODO: PPTQ Stuff
# Legalities in card output
# Rulings

rule_regexp = re.compile('(?:\d)+\.(?:.*)')
bot_attention_regex = re.compile('(?:!(\S*))+')


if __name__ == '__main__':
    def validate_colon_mode(s, loc, tokens):
        """Make sure colon modes are followed by a colon.

        TODO: n:One Two Three should probably be handled as n:"One Two Three"
        """
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

    # TODO
    # Difflib ratio
    # Foreign search
    # FRF boosters broken
    # DKA boosters broken
    # FUT boosters broken
    # Sealed pool generator

    # Rules parsing to include examples

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

    numCards = -1

    # Check if the database actually has stuff
    try:
        c.execute('SELECT COUNT(DISTINCT(name)) FROM cards')
        numCards = c.fetchone()[0]
        logging.debug("Found %d cards" % numCards)
    except sqlite.OperationalError:
        logging.error("No cards in DB? Try running dbimport.py")
        sys.exit(1)

    c.execute('SELECT DISTINCT(name) FROM cards')
    allCardNames = [y[0] for y in c.fetchall()]

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
        print r.text
        try:
            rj = r.json()
            user_pm_channel = rj['channel']
        except:
            print "Error parsing json"
            print sys.exc_info()
        return user_pm_channel

    def dispatch_message(message, channel):
        """For a message, figure out how to handle it and return the text to reply with.

        INPUT: message = Message string
        INPUT: channel = TRUE if message came from a main channel, FALSE if came from PM
        OUTPUT: (optional: list of) tuple of (reply_message, pm_override)
        OUTPUT: pm_override is TRUE if the reply should go through PM regardless

        If they give us "<string> extend", assume that it's "<cardname extend>".
        If they give us "<string>*", assume that it's "<cardname*>"
        """
        logging.debug("Dispatching message: %s" % message)
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
            cards = cardSearch(c, ['n:' + random.choice(allCardNames)])
            return (printCard(c, cards[0], quick=False, slackChannel=channel), False)
        elif message.endswith("extend"):
            cards = cardSearch(c, ['n:' + message[:-6].rstrip()])
            return (printCard(c, cards[0], extend=2, quick=False), True)
        elif message.endswith("*"):
            cards = cardSearch(c, ['n:' + message[:-1]])
            if len(cards) > 20:
                return ("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False)
            if channel:
                # If we've asked for some cards in a channel
                if len(cards) == 1:
                    # One card is fine, show them
                    return (printCard(c, cards[0], quick=False, slackChannel=channel), False)
                elif len(cards) <= 5:
                    # 2 - 5 cards is fine, but only show name and mana cost
                    return ("\n".join(["More than one result, changing to quick mode"] + [printCard(c, card, quick=True, slackChannel=channel) for card in cards]), False)
                else:
                    # > 5 is only showing name and mana cost and forced to PM
                    return [("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=channel) for card in cards]), True)]
            else:
                return ("\n".join([printCard(c, card, quick=False, slackChannel=channel) for card in cards] + ["{} result/s".format(len(cards))]), False)
        elif message.startswith("s ") or message.startswith("qs "):
            quick = False
            if message.startswith("qs "):
                quick = True
                card_name = message[3:].lower()
            else:
                card_name = message[2:].lower()
            output = []
            try:
                parsed_data = super_total.parseString(card_name)
            except (ParseException, ParseFatalException) as e:
                return "Unable to parse search terms\n%s" % e

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

            cards = cardSearch(c, output)
            if len(cards) > 20:
                return ("Too many cards to print! ({} > 20). Please narrow search".format(len(cards)), False)
            if channel:
                # If we've asked for some cards in a channel
                # If they're quick, <= 10 is fine
                if quick and len(cards) <= 10:
                    return ("\n".join([printCard(c, card, quick=quick, slackChannel=channel) for card in cards]), False)
                if len(cards) == 1:
                    # One card is fine, show them
                    return (printCard(c, cards[0], quick=quick, slackChannel=channel), False)
                elif len(cards) <= 5:
                    # 2 - 5 cards is fine, but only show name and mana cost
                    return ("\n".join(["More than one result, changing to quick mode"] + [printCard(c, card, quick=True, slackChannel=channel) for card in cards]), False)
                else:
                    # > 5 is only showing name and mana cost and forced to PM
                    return [("{} results sent to PM".format(len(cards)), False), ("\n".join([printCard(c, card, quick=True, slackChannel=channel) for card in cards]), True)]
            else:
                return ("\n".join([printCard(c, card, quick=quick, slackChannel=channel) for card in cards] + ["{} result/s".format(len(cards))]), False)
        elif message.startswith("r ") or rule_regexp.match(message):
            logging.debug("Rules query!")
            if message.startswith("r "):
                message = message[2:]
            return (ruleSearch(all_rules, message), False)
        else:
            logging.warning("Unparseable message :(")

    @listen_to('!(\S*)')
    def handle_public_message(message, card_name):
        """Listen to the channels, respond to something that looks like a command."""
        logging.debug("Received a public command.  Raw text: %s" % message.body['text'])
        message.reply("Channel command!")

    @respond_to('(.*)')
    def handle_private_message(message, message_text):
        """Receive a private message from the user and figure out how to respond."""
        logging.debug("Received private message.  Raw text: %s" % message.body['text'])
        if message_text.startswith("!"):
            logging.debug("Stripping leading !")
            message_text = message_text[1:]

        replies = dispatch_message(message_text.lower(), channel=False)
        if type(replies) is not list:
            replies = [replies]
        for reply in replies:
            message.reply(reply[0])

    def old_handle(message, card_name):
        """Place to hold old code."""
        command_list = bot_attention_regex.findall(message.body['text'])
        if command_list == []:
            command_list = [card_name]
        if message.body['text'].startswith("!") and message.body['text'][1:] != card_name:
            command_list.append(message.body['text'])
        # print "Found the following commands: " + str(command_list)
        # print "MBU: " + message.body['user']
        # print "Incoming Chan: " + message.channel._body.get('name', "")
        channel_message = (message.channel._body.get('name', "") != "")
        user_pm_channel = None
        print "Attempting to find preliminary PM channel"
        for channel_id, channel in iteritems(message._client.channels):
            if channel.get('user', "") == message.body['user']:
                print "Found PM channel"
                user_pm_channel = channel_id
                break
        for card_name in command_list:
            if card_name.startswith("!"):
                if user_pm_channel != message.body.get("channel", ""):
                    print "Channel Message starting with !"
                    if(card_name.endswith(' extend') or ('printsets' in card_name) or ('help' in card_name)):
                        print "Choosing to PM reply"
                        if not user_pm_channel:
                            print "Didn't get the prelim, doing the full thing"
                            user_pm_channel = send_user_pm(message.body['user'])
                        if user_pm_channel:
                            print "Found the thing"
                            message.body['channel'] = user_pm_channel
                        else:
                            print ":("
                            channel_message = True
                    else:
                        channel_message = True
            search = False
            quick = False
            extend = False
            if not search:
                test_list = ([x for x in allCardNames if difflib.SequenceMatcher(None, x.split(", ")[0].lower(), card_name.lower()).ratio() > 0.8])
                if test_list == []:
                    test_list = ([x for x in allCardNames if difflib.SequenceMatcher(None, x.lower(), card_name.lower()).ratio() >= 0.8])
                cards = c.execute('SELECT * FROM cards WHERE name = ? OR name = ? OR name IN (?) LIMIT 1', (card_name.strip(), gathererCapitalise(card_name.strip()), ",".join(test_list),)).fetchall()

            if cards != []:
                message_out = ""
                for card in cards:
                    message_out += printCard(card, quick=quick, extend=(2 if extend else 0), slackChannel=True) + '\n'
                if not channel_message:
                    message_out += '\n' + str(len(cards)) + " result/s"


    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

    bot = Bot()
    logging.debug("Bot instantiated")
    bot.run()
