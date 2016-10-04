#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
"""Frytherer Module.

This module contains all the helper functions for the
Frytherer command line interface and the Slackbot
"""
import ast, string, sys
from itertools import product
from operator import and_, or_
try:
    import re2 as re
except ImportError:
    import re
from fuzzywuzzy import process, fuzz
import logging
logging.basicConfig(level=logging.DEBUG)

mana_regexp = re.compile('([0-9]*)(b*)(g*)(r*)(u*)(w*)')
section_regexp = re.compile('a{0,1}(ipg|mtr) (?:(appendix [a-z])|(\d+)(?:(?:\.)(\d{1,2})){0,1})')
single_quoted_word = re.compile('^(?:\"|\')\w+(?:\"|\')$')


def gathererCapitalise(y):
    """
    Capitalise card names as Gatherer does.

    INPUT: Regular card name in whatever case
    OUTPUT: Magic style capitalised card name
    """
    words = y.split()
    ret_string = []
    for x in words:
        x = x.replace(u'\u2019', '\'').replace(u'\u2018', '\'').replace('`', '\'')
        if x not in ["of", "in", "to", "and", "the"]:
            ret_string.append(string.capwords(x))
        else:
            ret_string.append(x)

    return " ".join(ret_string)


def dedupe(seq, idfun=None):
    """
    It dedupes a sequence, and can take a custom function.

    I stole this from Stack Overflow
    """
    # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        try:
            marker = idfun(item)
        except AttributeError:  # pragma: no cover
            print item
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result


def calculateManaPerms(manaCost):
    """Calculate the possible mana permutations of cards.

    Used for hybrid cards when comparing mana costs)
    Input: Mana Cost of Card as a string (i.e {4}{U/G}{R/G})
    Output: Array of unique different mana cost combinations (i.e [4UR, 4UG, 4GR, 4GG])
    """
    manacost_permutes = []
    manacost_statics = []
    totalmanaoptions = []
    manacost_split = re.split("\{(.*?)\}+?", manaCost)

    for manaitem in manacost_split:
        if manaitem != '':
            if "/" in manaitem:
                manacost_permutes.append(manaitem.replace("/", ""))
            else:
                manacost_statics.append(manaitem)

    if manacost_permutes == []:
        totalmanaoptions.append("".join(manacost_statics))
    else:
        for x in product(*manacost_permutes):
            v = "".join(manacost_statics) + "".join(x)
            totalmanaoptions.append(''.join(sorted(v)))

    return dedupe(totalmanaoptions)


def calculateCMC(manaCost):
    """Calculate the converted mana cost of a mana cost string.

    It's expected to be sorted alphabetically
    Input: Mana Cost of Card as a string (i.e {4}{G}{G})
    Output: An int of the CMC (i.e 6)
    TODO: Handle Hybrid/Phyrexian
    """
    input_string = "".join(sorted(manaCost.replace("{", "").replace("}", "").lower()))
    input_array = mana_regexp.split(input_string)

    cmc = 0
    try:
        for idx, term in enumerate(input_array):
            if idx != 0 and idx != len(input_array) - 1:
                if input_array[idx] != '':
                    if idx == 1:
                        cmc += int(input_array[idx])
                    else:
                        cmc += len(input_array[idx])
    except:  # pragma: no cover
        logging.error("Some type of error calculating CMC. Tell Fry")
        logging.error(sys.exc_info())
    return cmc


def cardSearch(cursor, terms):
    """Search the database for cards.

    TODO: Parameterise the rest of this
    INPUT: Terms to search for, and the database cursor
    OUTPT: Card objects (if found)
    """
    params = []
    sql_query = "SELECT * FROM CARDS WHERE "
    do_later = []
    was_not = False
    for term in terms:
        if type(term) is not unicode:
            term = term.decode('utf-8')
        logging.debug("Processing term {}".format(term.encode("utf-8")))
        term = term.replace('"', '')
        if term.lower() in ["and", "or", "(", ")"]:
            sql_query += " " + term.upper() + " "
        if term.lower() == "not":
            sql_query += " NOT("
            was_not = True
        else:
            if term.startswith("banned:"):
                sql_query += "legalities LIKE ?"
                params.append("%u'legality': u'Banned', u'format': u'{}'%".format(term[7:].title()))
            elif term.startswith("legal:"):
                sql_query += "legalities LIKE ?"
                params.append("%u'legality': u'Legal', u'format': u'{}'%".format(term[6:].title()))
            elif term.startswith("restricted:"):
                sql_query += "legalities LIKE ?"
                params.append("%u'legality': u'Restricted', u'format': u'{}'%".format(term[11:].title()))
            elif term.startswith("set:"):
                sql_query += "(\"set\" = ? OR printings LIKE ?)"
                params.extend([term[4:], '%{}%'.format(term[4:].title())])
            elif term.startswith("cn:"):
                sql_query += "number LIKE ?"
                params.append(term[3:])
            elif term.startswith("pow") or term.startswith("tou"):
                # Need to do maths, so convert to number
                # TODO: Char Rumbler, and the 2+* type shit
                if term.startswith("pow"):
                    col = "power"
                else:
                    col = "toughness"
                operator = ""
                operand = ""
                if term[3] == ">" or term[3:].startswith("<"):
                    if term[4] == "=":
                        operator = term[3:5]
                        if term[5] == "*":
                            logging.error("Invalid P/T inequality")
                            continue
                        else:
                            operand = term[5:]
                    else:
                        operator = term[3]
                        if term[4] == "*":
                            logging.error("Invalid P/T inequality")
                            continue
                        else:
                            operand = term[4:]
                    if "cmc" not in operand and "pow" not in operand and "cmc" not in operand and "tou" not in operand:
                        try:
                            operand = int(operand)
                        except ValueError:  # pragma: no cover
                            logging.warning("Unable to convert power/toughness into an int")
                            continue
                    else:
                        operand = operand.replace("pow", "abs(power)").replace("tou", "abs(toughness)").replace("cmc", "abs(cmc)")
                    sql_query += "{} != '' AND abs({})".format(col, col) + operator + "?"
                    params.append(operand)
                elif term[3] == "=":
                    operator = term[3]
                    operand = term[4:]
                    #  Whitelist column names
                    if operand in ["cmc", "pow", "tou"]:
                        sql_query += col + operator + operand
                    else:
                        sql_query += col + operator + "?"
                        params.extend([operand.replace("pow", "power").replace("tou", "toughness")])
                else:  # pragma: no cover
                    # Should never get here
                    logging.error("Invalid power/toughness operator")
                    continue
            elif term.startswith("cmc"):
                sql_query += term.replace("pow", "power").replace("tou", "toughness").replace(":", "=")
            elif term.startswith("mana"):
                if term[4] == "=":
                    sql_query += "replace(replace(manacost, '}', ''), '{', '') = '" + term[5:].replace("{", "").replace("}", "").upper() + "'"
                elif term[4] == "!":
                    sql_query += "replace(replace(manacost, '}', ''), '{', '') LIKE '%" + term[5:].replace("{", "").replace("}", "") + "%'"
                else:
                    # Defer processing - can't do in SQL
                    do_later.append(term)
            elif term.startswith("n:"):
                sql_query += "name LIKE ?"
                params.append('%{}%'.format(term[2:]))
            elif term.startswith("en:"):
                sql_query += "name LIKE ?"
                params.append(term[3:])
            elif term.startswith("t:"):
                sql_query += "type LIKE ?"
                params.append('%{}%'.format(term[2:]))
            elif term.startswith("r:"):
                sql_query += "rarity = ?"
                params.append(term[2:].title())
            elif term.startswith("f:"):
                sql_query += "legalities LIKE ?"
                params.append("%u'legality': u'Legal', u'format': u'{}'%".format(term[2:].title()))
            elif term.startswith("a:"):
                sql_query += "artist LIKE ?"
                params.append('%{}%'.format(term[2:]))
            elif term.startswith("is:"):
                # normal, split, flip, double-faced, token, plane, scheme, phenomenon, leveler, vanguard
                if term[3:].lower() in ["split", "flip"]:
                    sql_query += "layout = ?"
                    params.append(term[3:].lower())
                elif term[3:] == "vanilla":
                    sql_query += "(text = '' AND types LIKE '%u''Creature''%')"
                elif term[3:] == "timeshifted":
                    sql_query += "(rarity = 'Special' AND printings LIKE '%Timeshifted%')"
                elif term[3:] == "funny":
                    sql_query += "(printings LIKE '%HHO%' OR printings LIKE '%UGL%' or printings LIKE '%UNH%')"
                elif term[3:] == "promo":
                    sql_query += "(source != '' AND source NOT LIKE '%Theme%')"
                elif term[3:] == "permanent":
                    sql_query += "(types LIKE '%Creature%' OR types LIKE '%Artifact%' OR types LIKE '%Enchantment%' OR types LIKE '%Planeswalker%' OR types LIKE '%Land%')"
                elif term[3:] == "spell":
                    sql_query += "(types LIKE '%Sorcery%' OR types LIKE '%Instant%')"
            elif term.startswith("c"):
                op = ""
                query_term = []
                if term[1] == "!":
                    op = " AND "
                elif term[1] == ":":
                    op = " OR "
                else:
                    print "Unable to parse colour string - unable to determine operator"
                    continue
                for y in term[2:]:
                    if y == 'w':
                        query_term.append("colors LIKE '%White%'")
                    if y == 'u':
                        query_term.append("colors LIKE '%Blue%'")
                    if y == 'b':
                        query_term.append("colors LIKE '%Black%'")
                    if y == 'r':
                        query_term.append("colors LIKE '%Red%'")
                    if y == 'g':
                        query_term.append("colors LIKE '%Green%'")
                    if y == 'm':
                        query_term.append("colors LIKE '%,%'")
                    if y == 'l':
                        query_term.append("types LIKE '%Land%'")
                    if y == 'c':
                        query_term.append("colors = '[]'")
                sql_query += "(" + op.join(query_term) + ")"
            elif term.startswith("o:"):
                sql_query += "text LIKE replace(?, '~', name)"
                params.append('%{}%'.format(term[2:]))
            if was_not:
                sql_query += ")"
                was_not = False

    # If empty for whatever reason
    if sql_query.endswith("AND ") or sql_query.endswith("WHERE "):
        sql_query += "1=1"
    sql_query += " GROUP BY name"
    logging.debug(sql_query)
    logging.debug(params)
    for (idx, param) in enumerate(params):
        if re.match(single_quoted_word, str(param.encode('utf-8'))):
            logging.debug("Single quoted word detected ({}), stripping".format(param))
            params[idx] = param[1:-1]
    logging.debug("Fixed: {}".format(params))
    cards = cursor.execute(sql_query, params).fetchall()
    if len(do_later) > 0:
        return_cards = []
        for term in do_later:
            if term.startswith("mana"):
                input_string = "".join(sorted(term[6:].replace("{", "").replace("}", "").lower()))
                input_array = mana_regexp.split(input_string)
                for card in cards:
                    if card["manacost"] == "":
                        continue
                    mana_costs = calculateManaPerms(card["manacost"].replace("W/P", "W").replace("U/P", "U").replace("B/P", "B").replace("R/P", "R").replace("G/P", "G"))
                    cmcret = False
                    manarets = []

                    for manacost in mana_costs:
                        manacost = manacost.encode('utf-8')
                        rets = []
                        mana_cost_string = "".join(sorted(manacost.replace("X", "0").lower()))
                        mana_cost_array = mana_regexp.split(mana_cost_string)
                        try:
                            for idx, t in enumerate(mana_cost_array):
                                if idx != 0 and idx != len(mana_cost_array) - 1:
                                    if term[4:].startswith(">="):
                                        if t >= input_array[idx]:
                                            rets.append(True)
                                        else:
                                            rets.append(False)
                                    elif term[4:].startswith("<="):
                                        if t <= input_array[idx]:
                                            rets.append(True)
                                        else:
                                            rets.append(False)
                                    elif term[4:].startswith(">"):
                                        if t > input_array[idx]:
                                            rets.append(True)
                                        else:
                                            rets.append(False)
                                    elif term[4:].startswith("<"):
                                        if t < input_array[idx]:
                                            rets.append(True)
                                        else:
                                            rets.append(False)
                            ret = reduce(and_, rets)
                            manarets.append(ret)
                        except IndexError:
                            print "Error: " + card["name"]
                    manarets = reduce(or_, manarets)
                    cmcret = None

                    # Calculate CMC of input string
                    cmc = calculateCMC(input_string)

                    # See if card only has generic mana
                    if len(ast.literal_eval(card["colors"])) == 0:
                        # If so, compare CMC of card to CMC of input string
                        if term[4:].startswith(">="):
                            if int(card["cmc"]) >= int(cmc):
                                cmcret = True
                            else:
                                cmcret = False
                        if term[4:].startswith("<="):
                            if int(card["cmc"]) <= int(cmc):
                                cmcret = True
                            else:
                                cmcret = False
                        if term[4:].startswith(">"):
                            if int(card["cmc"]) > int(cmc):
                                cmcret = True
                            else:
                                cmcret = False
                        if term[4:].startswith("<"):
                            if int(card["cmc"]) < int(cmc):
                                cmcret = True
                            else:
                                cmcret = False
                    else:
                        cmcret = False
                    if cmcret or manarets:
                        return_cards.append(card)
        return return_cards
    else:
        return cards


def printCard(cursor, card, extend=0, prepend="", quick=True, short=False, ret=False, slackChannel=False):
    """Given a card, return a formatted string fit for purpose."""
    types = ast.literal_eval(card["types"])
    names = ast.literal_eval(card["names"])
    colors = ast.literal_eval(card["colors"])
    supertypes = ast.literal_eval(card["supertypes"])
    subtypes = ast.literal_eval(card["subtypes"])
    printings = ast.literal_eval(card["printings"])
    rulings = ast.literal_eval(card["rulings"])
    legalities = ast.literal_eval(card["legalities"])

    if quick:
        try:
            if not short:
                return prepend + card["name"] + " (" + card["manaCost"] + ")"
            else:
                squished_rules_text = ""
                # Do some MODO-like compression of rules text to get it to fit
                if not ret:
                    squished_rules_text += prepend + card["name"]
                    if "/" in card["manaCost"]:
                        squished_rules_text += "(" + card["manaCost"] + ")"
                    else:
                        squished_rules_text += "(" + card["manaCost"].replace("{", "").replace("}", "") + ")"
                squished_rules_text += " ".join([x[0] for x in types])
                squished_rules_text += " - " + card["text"].replace("\n", ". ").replace(card["name"], "~").replace("{", "").replace("}", "")
                squished_rules_text = re.sub('\(.*?\)', '', squished_rules_text)
                squished_rules_text = squished_rules_text.replace("They can't be regenerated.", "No regen.").replace("It can't be regenerated.", "No regen.")
                squished_rules_text = squished_rules_text.replace("Regenerate", "Regen").replace("acrifice", "ac")
                squished_rules_text = squished_rules_text.replace("arget", "gt").replace("raveyard", "y")
                squished_rules_text = squished_rules_text.replace("Search your library for", "Tutor").replace("search your library for", "tutor")
                squished_rules_text = squished_rules_text.replace("converted mana cost", "CMC")
                squished_rules_text = squished_rules_text.replace("end of turn", "EOT").replace("enters the battlefield", "ETB")
                squished_rules_text = squished_rules_text.replace("less than or equal to", "<=").replace("greater than or equal to", ">=")
                squished_rules_text = squished_rules_text.replace("less than", "<").replace("greater than", ">").replace("more than", ">")
                squished_rules_text = squished_rules_text.replace("is equal to", "=").replace("equal to", "=").replace(" and ", " & ")
                squished_rules_text = squished_rules_text.replace(" one ", " 1 ").replace(" two ", " 2 ").replace(" three ", " 3 ").replace(" four ", " 4 ").replace(" five ", " 5 ")
                squished_rules_text = squished_rules_text.replace("battlefield", "bf").replace("opponent", "opp").replace("damage", "dmg").replace("permanent", "perm")
                squished_rules_text = squished_rules_text.replace("Draw a card, then discard a card", "Loot").replace("discard a card", "discard").replace("draw a card", "cantrip").replace("Draw a card", "Cantrip")
                squished_rules_text = squished_rules_text.replace("any time you could cast a sorcery", "WRAPS").replace("becomes", "=").replace("where X is", "X =")
                squished_rules_text = squished_rules_text.replace("power", "pow").replace("toughness", "tou").replace("that card", "it").replace("that creature", "it")
                squished_rules_text = squished_rules_text.replace("Return it to your hand", "Bounce").replace("rotection from", "ro").replace("huffle your library", "huffle")
                squished_rules_text = squished_rules_text.replace("his or her", "their").replace("to your mana pool", "").replace("source", "src")
                squished_rules_text = squished_rules_text.replace("artifact", "art").replace("creature", "crt").replace("token", "tkn").replace("ounter", "tr").replace("ontrol", "trl")
                squished_rules_text = squished_rules_text.replace("nstant", "nst").replace("orcery", "orc")
                squished_rules_text = squished_rules_text.replace(" white ", " W ").replace(" White ", " W ")
                squished_rules_text = squished_rules_text.replace(" blue ", " U ").replace(" Blue ", " U ")
                squished_rules_text = squished_rules_text.replace(" black ", " B ").replace(" Black ", " B ")
                squished_rules_text = squished_rules_text.replace(" red ", " R ").replace(" Red ", " R ")
                squished_rules_text = squished_rules_text.replace(" green ", " G ").replace(" Green ", " G ")
                squished_rules_text = re.sub('put the top (\d+) cards of your library into your gy', 'mill \g<1>', squished_rules_text)
                squished_rules_text = re.sub('Return (.*?) to (their owners\'|its owner\'s) (hand|hands)', 'Bounce \g<1>', squished_rules_text)
                squished_rules_text = re.sub('(pow|tou|CMC) (\d+) or greater', '\g<1> >= \g<2>', squished_rules_text)
                if "Creature" in types:
                    squished_rules_text += " - " + card["power"] + "/" + card["toughness"]

                if ret:
                    return card["name"] + " (" + card["manaCost"] + ")" + "- " + " - ".join([squished_rules_text.replace(". . ", ". ").replace("..", ".").replace("-  - ", " - ").replace("  ", " ")])
                return "- " + " - ".join([squished_rules_text.replace(". . ", ". ").replace("..", ".").replace("-  - ", " - ").replace("  ", " ")])
        except AttributeError:  # pragma: no cover
            logging.error("Error when printing card")
            logging.error(card)
            logging.error(sys.exc_info())
            return card + " " + str(sys.exc_info())
    else:
        message_out = ""
        message_out += ("*" if slackChannel else "") + card["name"] + ("* " if slackChannel else '\n')
        if(names):
            message_out += "(Part of " + " // ".join(names) + ")" + (" " if slackChannel else '\n')
        if(card["manaCost"]):
            message_out += card["manaCost"] + (" " if slackChannel else '\n')
            if not any(word in card["manaCost"] for word in "W U B R G") and colors != []:
                message_out += ", ".join(colors) + (" " if slackChannel else '\n')
        else:
            message_out += ", ".join(colors) + ("" if slackChannel else '\n')
        message_out += ("|" if slackChannel else "") + " ".join(supertypes) + (" " if supertypes else "") + " ".join(types) + (" - " if subtypes else "") + " ".join(subtypes) + ("| " if slackChannel else '\n')
        if "Creature" in types:
            message_out += card["power"] + "/" + card["toughness"] + (" " if slackChannel else '\n')
        if "Planeswalker" in types:
            message_out += "[" + str(card["loyalty"]) + "]" + ("  " if slackChannel else '\n')
        if slackChannel:
            message_out += card["text"].replace('\n', ' / ')
        else:
            message_out += card["text"] + '\n'
    if extend:
        message_out += "----------" + '\n'
        sources = cursor.execute('SELECT "set", source, rarity, starter, artist, flavor, number FROM cards WHERE name = ?', (card["name"],)).fetchall()
        for p in printings:
            setcode = cursor.execute('SELECT name FROM sets WHERE code = ?', (p,)).fetchone()
            source = next(x for x in sources if x[0] == p)
            message_out += setcode[0] + " (" + source[2] + ")" + ((" (" + source[6] + ")") if source[6] else "") + ((" (" + source[1] + ")") if source[1] else "") + (" (Starter Pack)" if source[3] else "") + " [" + source[4] + "]" + '\n'
            if source[5]:
                message_out += source[5] + '\n'
        message_out += "----------" + '\n'
        if extend > 0:
            # if card["originalText"] != "" and (card["originalText"] != card["text"]):
            #    message_out += "-----------\n" + '\n'
            #    message_out += card["originalText"] + '\n'
            #    message_out += card["originalType"] + '\n'
            #    message_out += "-----------\n" + '\n'
            if rulings != []:
                message_out += "----------" + '\n'
                for rule in rulings:
                    message_out += rule["text"] + "\n"
                message_out += "----------\n"
            if legalities != []:
                for l in legalities:
                    message_out += l["format"] + " : " + l["legality"] + '\n'
                message_out += "----------" + '\n'
            dbForeignNames = cursor.execute('SELECT foreignNames FROM cards WHERE name = ?', (card["name"],)).fetchall()
            foreignNames = {}
            for dbNameList in dbForeignNames:
                if dbNameList[0] != '[]':
                    nameList = ast.literal_eval(dbNameList[0])
                    for name in nameList:
                        foreignNames[name["language"]] = name["name"]

            for fPrint in foreignNames.items():
                message_out += fPrint[0] + " : " + fPrint[1] + '\n'
    return message_out.rstrip()


def cardExtendSearch(matches, command, ret, finalCard):
    """ Take a card and command input, and output either the flavor or gatherer rulings of that card

    matches is a list of the matches for our gatherRuling regex, pulling out name and num
    command is either flavor or ruling, to tell us which to return
    ret is our return string, to which we should append our text (don't overwrite)
    finalCard is a dictionary of all the attributes of our card as matched by guessCard."""
    # Set all our variables for checking later
    rulings = []
    flavor = ""
    # The SQL return is a string, but can be eval'd into a list
    logging.debug("Card is {}".format(finalCard["name"]))
    if command.startswith("ruling"):
        rulings = ast.literal_eval(finalCard["rulings"])
    elif command.startswith("flavo"):
        flavor = finalCard["flavor"]
    if rulings != [] or flavor != "":
        # Do we have a ruling number
        if matches["num"] is not None:
            # We do
            # In case of out of index, try with except
            if 0 <= matches["num"] < len(rulings):
                logging.debug("Returning rule number {}".format(str(matches["num"])))
                ret.append(("{} - {}".format(finalCard["name"], rulings[matches["num"]]["text"]), False))
                return ret
            # Out of Index
            else:
                logging.debug("That's not a rule!")
                if len(rulings) == 0:
                    response = "There are no rulings for this card"
                elif len(rulings) == 1:
                    response = "This card only has one ruling"
                elif len(rulings) > 1:
                    response = "Valid rulings are 1 - {}".format(len(rulings))
                ret.append(("That's not a rule for {}! {}".format(finalCard["name"], response), False))
                return ret
        else:
            # We don't, it could be flavor, or multiple rules
            if len(rulings) > 1:  # Check how many rules. if >1, obviously not flavor
                logging.debug("No rule number, returning all rules")
                # Too many rulings, send to PM instead
                ret.extend([("{} rulings sent to PM".format(len(rulings)), False), ("\n".join([finalCard["name"]]), True)])
                rulingstring = ""
                # Add to string to avoid spam messages
                x = 1  # Number the rulings
                for x, rule in enumerate(rulings, start=1):
                    rulingstring = "{}\n{}. {}".format(rulingstring, x, rule["text"])
                # Create return string
                rulingstring = "{}\n{}".format(rulingstring, "To show a single ruling in the channel, use the command `!ruling <card> <ruling number>`")
                ret.append((rulingstring, True))
                return ret
            else:  # Could be flavor or ruling with one rule
                if rulings != []:
                    logging.debug("No rule number, but only one rule")
                    string = rulings[0]["text"]
                else:
                    logging.debug("Returning Flavour Text")
                    string = flavor
                ret.append(("{} - {}".format(finalCard["name"], string), False))
                return ret
    else:
        # No return!
        if command.startswith("ruling"):
            ret.append(("{} has no rulings on Gatherer".format(finalCard["name"]), False))
        elif command.startswith("flavo"):
            ret.append(("{} has no flavour text!".format(finalCard["name"]), False))
        return ret


def ruleSearch(all_rules, rule_to_search):
    """Search the rules of the game.

    INPUT: A rule number, or text
    OUTPUT: The rule number and text of the matching rule
    """
    if all_rules == {}:
        return "Rules search not available"

    rule_to_search = gathererCapitalise(rule_to_search)

    # print process.extract(rule_to_search, all_rules.keys(), scorer=fuzz.ratio)
    # print process.extract(rule_to_search, all_rules.keys(), scorer=fuzz.partial_ratio)
    # print process.extract(rule_to_search, all_rules.keys(), scorer=fuzz.token_sort_ratio)
    # print process.extract(rule_to_search, all_rules.keys(), scorer=fuzz.token_set_ratio)

    # Just fucken special case it
    # if rule_to_search == "die":
    #    rule_to_search = "dies"

    backup_rule = process.extract(rule_to_search, all_rules.keys(), scorer=fuzz.token_set_ratio)
    logging.debug("Preprocess: {}".format(backup_rule))
    backup_rule = filter(lambda x: x[1] >= 80 and len(x[0]) > 3, backup_rule)
    if not backup_rule:
        prefix_check = [v for v in all_rules.keys() if v.startswith(rule_to_search)]
        if len(prefix_check) == 1:
            backup_rule = [(prefix_check[0], 100)]
    logging.debug("Rules Query for {}.  Found backup/s? {}".format(rule_to_search, backup_rule))
    if rule_to_search in all_rules or backup_rule:
        if rule_to_search not in all_rules and backup_rule:
            logging.debug("Using backup")
            # Tie breaker
            if len(backup_rule) == 2 and backup_rule[0][1] == 100 and backup_rule[1][1] == 100:
                best = process.extractOne(rule_to_search, all_rules.keys(), scorer=fuzz.token_sort_ratio)
            else:
                # Give me the highest score, breaking ties by the shortest length
                best = max(backup_rule, key=lambda x: (x[1], len(x[0]) * -1))
            rule_to_search = best[0]
        if "." not in rule_to_search and rule_to_search + ".1" in all_rules:
            # Give them back the one after the heading too
            logging.debug("Detected heading, giving more")
            return [rule_to_search + ": " + all_rules[rule_to_search], rule_to_search + ".1" + ": " + all_rules[rule_to_search + ".1"]]
        if re.match(r'([^0-9]+)', rule_to_search) and "See rule" in all_rules[rule_to_search] and "See rules" not in all_rules[rule_to_search] and "and rule" not in all_rules[rule_to_search] and "and section" not in all_rules[rule_to_search]:
            # Give them back the referenced rule too
            ref_ruled = re.search(r'See rule (\d+\.{0,1}\d*)', all_rules[rule_to_search])
            if ref_ruled:
                new_rule = ref_ruled.group(1)
                logging.debug("Detected glossary, giving reference of {}".format(new_rule))
                if new_rule in all_rules:
                    # Prefer a more specific rule
                    if new_rule + "a" in all_rules:
                        new_rule = new_rule + "a"
                    elif re.match(r'\d{3}', new_rule) and new_rule + ".1" in all_rules:
                        new_rule = new_rule + ".1"
                    return [rule_to_search + ": " + all_rules[rule_to_search], new_rule + ": " + all_rules[new_rule]]
        return (rule_to_search + ": " + all_rules[rule_to_search])
    else:
        rules_list = [(x, y) for (x, y) in all_rules.items() if re.search(re.escape(rule_to_search), y, re.I)]
        for (rule_no, rule) in sorted(rules_list):
            return (str(rule_no) + ": " + rule)
    return "No rule/s found"


def help():
    """Print out help message."""
    ret = ""
    ret += "Welcome to Frytherer.  Your options are:\n"
    ret += "<card name> - gives what's on the card\n"
    ret += "<card name> extend - gives extended info about the card (everything - rulings, legality, artist, flavour text, foreign names)\n"
    ret += "<card name>* - search card names\n"
    ret += "r <text> - search the comprehensive rules for text\n"
    ret += "s <text> - advanced search for cards with particular characteristics.  Type helpsearch for info\n"
    ret += "qs <text> - same as above but only give card names\n"
    ret += "random - gives a random card\n"
    ret += "printsets - gives a list of all the sets I know about\n"
    ret += "printsetsinorder - gives a list of all the sets in release date order\n"
    ret += "url <cr|(a)mtr <section>|(a)ipg <section>|<infraction>|jar|peip|pptq|rptq|alldocs> - gives the URL to the requested document\n"
    ret += "flavour <card> - gives flavour text of a card.\n"
    ret += "ruling <card> [number] - gives a specific Gatherer ruling of a card.\n"
    # ret += "\tallcards <set> - gives a list of all the cards with a given set code (use printsets to get the code)\n"
    # ret += "\tallcardsextend <set> - gives the text of all the cards with a given set code (use printsets to get the code)\n"
    # ret += "\tbooster <set> - gives a randomly generated booster from either set code, or set name\n"
    # ret += "\tqbooster <set> - gives a randomly generated booster from either set code, or set name, short names\n"
    ret += "help - prints this help\n"
    ret += "Any bugs, questions, or suggestions - ask Fry!\n"
    return ret


def helpsearch():
    """Print out advanced search help message."""
    return """All these options can be combined to more complicated queries: "a or b", "a not b", "a (b or c)", "a or (b c)", and so on.
        Options prepended with '#' are not yet implemented

        Name:
            n:Birds of Paradise
            cn:(Collector Number)
        Rules Text (Oracle):
            o:Flying
            o:"First strike"
            o:{T} o:"add one mana of any color"
            (new) o:"whenever ~ deals combat damage"
        Types (Oracle):
            t:angel
            t:"legendary angel"
            t:basic
            t:"arcane instant"
        Colors:
            c:w (Any card that is white)
            c:wu (Any card that is white or blue)
            c:wum (Any card that is white or blue, and multicolored)
            c!w (Cards that are only white)
            c!wu (Cards that are only white or blue, or both)
            c!wum (Cards that are only white and blue, and multicolored)
            c!wubrgm (Cards that are all five colors)
            c:m (Any multicolored card)
            c:l or c:c (Lands and colorless cards)
        # Color Identity:
        #     ci:wu (Any card that is white or blue, but does not contain any black, red or green mana symbols)
        # Color Indicator:
        #     in:wu (Any card that is white or blue according to the color indicator.)
        Mana Cost:
            mana=3G (Spells that cost exactly 3G, or split cards that can be cast with 3G)
            mana>=2WW (Spells that cost at least two white and two colorless mana)
            mana<GGGGGG (Spells that can be cast with strictly less than six green mana)
            mana>=2RR mana<=6RR (Spells that cost two red mana and between two and six colorless mana)
            # mana>={2/R}
            # mana>={W/U}
            # mana>={U/P}
            mana!{G}{G} (Spells whose mana cost contains {G}{G})
            mana!P (Spells whose mana cost contains Phyrexian mana)
        Power, Toughness, Converted Mana Cost:
            pow>=8
            tou<pow (All combinations are possible)
            cmc=7
        Rarity:
            r:mythic
        Format:
            f:standard (or block, extended, vintage, classic, legacy, modern, commander)
            banned:extended (or legal, restricted)
            set:TPR
        Artist:
            a:"rk post"
        Is:
            is:split, is:flip
            is:vanilla (Creatures with no card text)
            # is:old, is:new, is:future (Old/new/future card face)
            is:timeshifted
            is:funny, not:funny (Unglued/Unhinged/Happy Holidays Promos)
            is:promo (Promotional cards)
            is:promo is:old (Promotional cards with the original card face)
            is:permanent, is:spell
            # is:black-bordered, is:white-bordered, is:silver-bordered
    """


def url(document):
    """Work out the appropriate URL and return it to the user."""
    logging.debug("Serving URL: {}".format(document))
    if document.startswith("url "):
        document = document[4:]
        logging.debug("Formatting: {}".format(document))
    doc_words = document.split()
    ret = ""

    if doc_words[0] == "jar":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_jar_4.pdf"
    elif doc_words[0] == "peip":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_peip-16_16feb8_en.pdf"
    elif doc_words[0] == "cr":
        ret = "http://yawgatog.com/resources/magic-rules/"
    elif doc_words[0] == "alldocs":
        ret = "http://wpn.wizards.com/en/resources/rules-documents"
    elif doc_words[0] == "pptq":
        ret = "http://magic.wizards.com/en/events/instoreplay/pptqaer"
    elif doc_words[0] == "rptq":
        ret = "http://magic.wizards.com/en/events/instoreplay/rptqaer"
    elif doc_words[0] == "mt" or " ".join(doc_words[0:2]) == "missed trigger":
        ret = "http://blogs.magicjudges.org/rules/ipg2-1/"
    elif doc_words[0] == "l@ec" or doc_words[0] == "lec" or " ".join(document[0:3]) == "looking at extra cards":
        ret = "http://blogs.magicjudges.org/rules/ipg2-2/"
    elif doc_words[0] == "hce" or " ".join(document[0:2]) == "hidden card error":
        ret = "http://blogs.magicjudges.org/rules/ipg2-3/"
    elif doc_words[0] == "mpe" or " ".join(document[0:3]) == "mulligan procedure error":
        ret = "http://blogs.magicjudges.org/rules/ipg2-4/"
    elif doc_words[0] == "grv" or " ".join(document[0:3]) == "game rule violation":
        ret = "http://blogs.magicjudges.org/rules/ipg2-5/"
    elif doc_words[0] == "ftmgs" or " ".join(document[0:4]) == "failure to maintain game state":
        ret = "http://blogs.magicjudges.org/rules/ipg2-6/"
    elif doc_words[0] == "tardiness":
        ret = "http://blogs.magicjudges.org/rules/ipg3-1/"
    elif doc_words[0] == "oa" or " ".join(doc_words[0:2]) == "outside assistance":
        ret = "http://blogs.magicjudges.org/rules/ipg3-2/"
    elif " ".join(doc_words[0:2]) == "slow play":
        ret = "http://blogs.magicjudges.org/rules/ipg3-3/"
    elif " ".join(doc_words[0:2]) == "insufficient shuffling":
        ret = "http://blogs.magicjudges.org/rules/ipg3-4/"
    elif doc_words[0] == "ddlp" or doc_words[0] == "d/dlp" or ("deck" in document and "problem" in document):
        ret = "http://blogs.magicjudges.org/rules/ipg3-5/"
    elif doc_words[0] == "lpv" or " ".join(document[0:3]) == "limited procedure violation":
        ret = "http://blogs.magicjudges.org/rules/ipg3-6/"
    elif doc_words[0] == "cpv" or " ".join(document[0:3]) == "communication policy violation":
        ret = "http://blogs.magicjudges.org/rules/ipg3-7/"
    elif doc_words[0] == "mc" or " ".join(document[0:2]) == "marked cards":
        ret = "http://blogs.magicjudges.org/rules/ipg3-8/"
    elif doc_words[0] == "usc" or " ".join(document[0:2]) == "unsporting conduct":
        if "minor" in document:
            ret = "http://blogs.magicjudges.org/rules/ipg4-1/"
        elif "major" in document:
            ret = "http://blogs.magicjudges.org/rules/ipg4-2/"
    elif doc_words[0] == "idaw" or " ".join(document[0:4]) == "improperly determining a winner":
        ret = "http://blogs.magicjudges.org/rules/ipg4-3/"
    elif doc_words[0] == "bribery":
        ret = "http://blogs.magicjudges.org/rules/ipg4-4/"
    elif doc_words[0] == "ab" or doc_words[0] == "aggressive":
        ret = "http://blogs.magicjudges.org/rules/ipg4-5/"
    elif doc_words[0] == "totm" or doc_words[0] == "theft":
        ret = "http://blogs.magicjudges.org/rules/ipg4-6/"
    elif doc_words[0] == "stalling":
        ret = "http://blogs.magicjudges.org/rules/ipg4-7/"
    elif doc_words[0] == "cheating":
        ret = "http://blogs.magicjudges.org/rules/ipg4-8/"
    elif section_regexp.match(document):
        try:
            logging.debug("URL Section Match detected")
            (doco, appendix, main, sub) = (section_regexp.match(document)).groups()
            logging.debug("Doco: {} Appendix: {} Main: {} Sub: {}".format(doco, appendix, main, sub))
            if doco == "ipg":
                if appendix:
                    (app, letter) = appendix.split(None, 2)
                    if (letter != "a" and letter != "b"):
                        ret = "Invalid section requested"
                    else:
                        ret = "http://blogs.magicjudges.org/rules/ipg-%s-%s/" % (app, letter)
                    return ret
                main = int(main)
                if (main >= 1) and (main <= 4):
                    if sub is None:
                        ret = "http://blogs.magicjudges.org/rules/ipg%d/" % main
                    else:
                        sub = int(sub)
                        if(
                            (main == 1 and (sub >= 1 and sub <= 4)) or
                            (main == 2 and (sub >= 1 and sub <= 6)) or
                            (main == 3 and (sub >= 1 and sub <= 8)) or
                            (main == 4 and (sub >= 1 and sub <= 8))
                        ):
                            ret = "http://blogs.magicjudges.org/rules/ipg%d-%d/" % (main, sub)
                        else:
                            ret = "Invalid section requested"
                else:
                    ret = "Invalid section requested"
            elif doco == "mtr":
                if appendix:
                    (app, letter) = appendix.split()
                    if(letter != "a" and letter != "b" and letter != "c" and letter != "d" and letter != "e" and letter != "f"):
                        ret = "Invalid section requested"
                    else:
                        ret = "http://blogs.magicjudges.org/rules/mtr-%s-%s/" % (app, letter)
                    return ret
                main = int(main)
                if (main >= 1 and main <= 10):
                    if sub is None:
                        ret = "Invalid section requested"
                    else:
                        sub = int(sub)
                        if(
                            (main == 1 and (sub >= 1 and sub <= 12)) or
                            (main == 2 and (sub >= 1 and sub <= 14)) or
                            (main == 3 and (sub >= 1 and sub <= 15)) or
                            (main == 4 and (sub >= 1 and sub <= 5)) or
                            (main == 5 and (sub >= 1 and sub <= 5)) or
                            (main == 6 and (sub >= 1 and sub <= 7)) or
                            (main == 7 and (sub >= 1 and sub <= 7)) or
                            (main == 8 and (sub >= 1 and sub <= 6)) or
                            (main == 9 and (sub >= 1 and sub <= 7)) or
                            (main == 10 and (sub >= 1 and sub <= 4))
                        ):
                            ret = "http://blogs.magicjudges.org/rules/mtr%d-%d/" % (main, sub)
                        else:
                            ret = "Invalid section requested"
                else:
                    ret = "Invalid section requested"
            else:
                ret = "Something went wrong parsing your request"
        except:  # pragma: no cover
            logging.debug(sys.exc_info())
            ret = "Something went wrong parsing your request"
    elif doc_words[0] == "mtr":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_mtr_30sep16_en.pdf"
    elif doc_words[0] == "ipg":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_ipg_30sep16_en.pdf"
    elif doc_words[0] == "aipg":
        ret = "http://blogs.magicjudges.org/rules/ipg/"
    elif doc_words[0] == "amtr":
        ret = "http://blogs.magicjudges.org/rules/mtr/"
    else:
        ret = "I didn't understand what document you wanted"
    return ret
