#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import json, re, rlcompleter, random, sys
from pyparsing import *
import signal, ast, string
from itertools import product
from operator import and_, or_
import pysqlite2.dbapi2 as sqlite
from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to

def gathererCapitalise(y):
    words = y.split(" ")
    ret_string = []
    for x in words:
        x = x.replace(u'\u2019', '\'').replace(u'\u2018', '\'').replace('`', '\'')
        if x not in ["of", "in", "to", "and", "the"]:
            ret_string.append(string.capwords(x))
        else:
            ret_string.append(x)

    return " ".join(ret_string)

def dedupe(seq, idfun=None):
        # order preserving
    if idfun is None:
        def idfun(x): return x
    seen = {}
    result = []
    for item in seq:
        try:
            marker = idfun(item)
        except AttributeError:
            print item
        # in old Python versions:
        # if seen.has_key(marker)
        # but in new ones:
        if marker in seen: continue
        seen[marker] = 1
        result.append(item)
    return result

mana_regexp = re.compile('([0-9]*)(b*)(g*)(r*)(u*)(w*)')
rule_regexp = re.compile('(?:\d)+\.(?:.*)')

# Calculate the possible mana permutations of cards
# Used for hybrid cards when comparing mana costs)
# Input: Mana Cost of Card as a string (i.e {4}{U/G}{R/G})
# Output: Array of unique different mana cost combinations (i.e [4UR, 4UG, 4GR, 4GG])
def calculateManaPerms(manaCost):
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
            s = -1
            ret = ""
            for i in v:
                try:
                    s += int(i)
                except ValueError:
                    ret += i
            totalmanaoptions.append(ret + (str(s) if s != -1 else ""))

    return dedupe(totalmanaoptions)

# Calculate the converted mana cost of a mana cost string
# It's expected to be sorted alphabetically
# Input: Mana Cost of Card as a string (i.e {4}{G}{G})
# Output: An int of the CMC (i.e 6)
# TODO: Handle Hybrid/Phyrexian
def calculateCMC(manaCost):
    input_string = "".join(sorted(manaCost.replace("{", "").replace("}", "").lower()))
    input_array = mana_regexp.split(input_string)

    cmc = 0
    try:
        for idx, term in enumerate(input_array):
            if idx != 0 and idx != len(input_array)-1:
                if input_array[idx] != '':
                    if idx == 1:
                        cmc += int(input_array[idx])
                    else:
                        cmc += len(input_array[idx])
    except:
        print "Some type of error calculating CMC. Tell Fry"
        print sys.exc_info()
    return cmc


def new_filter_function(terms):
    sql_query = "SELECT * FROM CARDS WHERE "
    do_later = []
    was_not = False
    for term in terms:
        if term.lower() in ["and", "or", "(", ")"]:
            sql_query += " " + term.upper() + " "
        if term.lower() == "not":
            sql_query += " NOT("
            was_not = True
        else:
            if term.startswith("banned:"):
                sql_query += "legalities LIKE '%u''legality'': u''Banned'', u''format'': u''" + term[7:].title() + "''%'"
            elif term.startswith("legal:"):
                sql_query += "legalities LIKE '%u''legality'': u''Legal'', u''format'': u''" + term[6:].title() + "''%'"
            elif term.startswith("restricted:"):
                sql_query += "legalities LIKE '%u''legality'': u''Restricted'', u''format'': u''" + term[11:].title() + "''%'"
            elif term.startswith("set:"):
                sql_query += "(\"set\" = '" + term[4:] + "' OR printings LIKE '%" + term[4:].title() + "%')"
            elif term.startswith("cn:"):
                sql_query += "number LIKE " + term[3:]
            elif term.startswith("pow"):
                # Need to do maths, so convert to number
                if term[3:].startswith(">") or term[3:].startswith("<"):
                    if term[4] == "=":
                        if term[5] == "*":
                            print "Invalid P/T inequality"
                    else:
                        if term[4] == "*":
                            print "Invalid P/T inequality"
                    sql_query += "abs(power)" + term[3:].replace("pow", "abs(power)").replace("tou", "abs(toughness)").replace("cmc", "abs(cmc)")
                else:
                    sql_query += "power" + term[3:].replace("pow", "power").replace("tou", "toughness").replace(":", "=")
            elif term.startswith("tou"):
                sql_query += "toughness" + term[3:].replace("pow", "power").replace("tou", "toughness").replace("cmc", "abs(cmc)").replace(":", "=")

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
                sql_query += "name LIKE '%" + term[2:].replace('"', '') + "%'"
            elif term.startswith("t:"):
                sql_query += "type LIKE '%" + term[2:].replace('"', '') + "%'"
            elif term.startswith("r:"):
                sql_query += "rarity = '" + term[2:].replace('"', "").title() + "'"
            elif term.startswith("f:"):
                sql_query += "legalities LIKE '%u''legality'': u''Legal'', u''format'': u''" + term[2:].title() + "''%'"
            elif term.startswith("a:"):
                sql_query += "artist LIKE '%" + term[2:].replace('"', "") + "%' "
            elif term.startswith("is:"):
                # normal, split, flip, double-faced, token, plane, scheme, phenomenon, leveler, vanguard
                if term[3:].lower() in ["split", "flip"]:
                    sql_query += "layout = " + term[3:].lower()
                elif term[3:] == "vanilla":
                    sql_query += "(text = '' AND types LIKE '%u''Creature''%')"
                elif term[3:] == "timeshifted":
                    sql_query += "(rarity = 'Special' AND printings LIKE '%Timeshifted%')"
                elif term[3:] == "funny":
                    sql_query += "(printings LIKE '%Happy Holidays%' OR printings LIKE '%Unglued%' or printings LIKE '%Unhinged%')"
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
                sql_query += "text LIKE replace('%" + term[2:].replace('"', '') + "%', '~', name)"
            if was_not:
                sql_query += ")"
                was_not = False

    # If empty for whatever reason
    if sql_query.endswith("AND ") or sql_query.endswith("WHERE "):
        sql_query += "1=1"
    sql_query += " GROUP BY name"
    print sql_query
    cards = c.execute(sql_query).fetchall()
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
                                if idx != 0 and idx != len(mana_cost_array)-1:
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

if __name__ == '__main__':
    colon_mode = oneOf("n o t cn in pow tou cmc r f a banned legal restricted is set")
    colon_or_bang_mode = "c"
    math_mode = oneOf("mana pow tou cmc")
    colon_operator = ":"
    bang_operator = "!"
    math_operator = oneOf("= >= > <= < !")
    boolean_operators = oneOf("and not or")
    brackets = oneOf("( )")
    operand = (Word(alphanums) | dblQuotedString | OneOrMore(Combine(Literal("{") + Word(alphanums+"\\") + Literal("}"))))

    colon_total = colon_mode + colon_operator
    colon_or_bang_total = colon_or_bang_mode + oneOf([colon_operator, bang_operator])
    math_total = math_mode + math_operator

    total_thing = Combine( (colon_total | colon_or_bang_total | math_total) + operand )
    super_total = OneOrMore(Optional(OneOrMore(boolean_operators)) + Optional(OneOrMore(brackets)) + total_thing + Optional(OneOrMore(brackets)) + Optional(OneOrMore(boolean_operators)))

    def safe_list_get (l, idx, default):
        try:
            if l[idx] != None:
                return l[idx]
            else:
                return ""
        except IndexError:
            return default

    def printCard(card, extend=0, prepend="", quick=True, short=False, ret=False, slackChannel=False):
        Types = ast.literal_eval(card["types"])
        Names = ast.literal_eval(card["names"])
        Colors = ast.literal_eval(card["colors"])
        Supertypes = ast.literal_eval(card["supertypes"])
        Subtypes = ast.literal_eval(card["subtypes"])
        Printings = ast.literal_eval(card["printings"])
        Rulings = ast.literal_eval(card["rulings"])
        Legalities = ast.literal_eval(card["legalities"])

        if quick:
            try:
                if not short:
                    return prepend + card["name"] + " (" + card["manaCost"] + ")"
                else:
                    squished_rules_text = ""
                    # Do some MODO-like compression of rules text to get it to fit
                    if not ret:
                        squished_rules_text += prepend + card["name"],
                        if "/" in card["manaCost"]:
                            squished_rules_text += "(" + card["manaCost"] + ")",
                        else:
                            squished_rules_text += "(" + card["manaCost"].replace("{", "").replace("}", "") + ")",
                    squished_rules_text += " ".join([x[0] for x in Types])
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
                    squished_rules_text = squished_rules_text.replace(" red ",  " R ").replace(" Red ", " R ")
                    squished_rules_text = squished_rules_text.replace(" green ", " G ").replace(" Green ", " G ")
                    squished_rules_text = re.sub('put the top (\d+) cards of your library into your gy', 'mill \g<1>', squished_rules_text)
                    squished_rules_text = re.sub('Return (.*?) to (their owners\'|its owner\'s) (hand|hands)', 'Bounce \g<1>', squished_rules_text)
                    squished_rules_text = re.sub('(pow|tou|CMC) (\d+) or greater', '\g<1> >= \g<2>', squished_rules_text)
                    if "Creature" in Types:
                        squished_rules_text += " - " + card["power"] + "/" + card["toughness"]

                    if ret:
                        return card["name"] + " (" + card["manaCost"] + ")" + "- " + " - ".join([squished_rules_text.replace(". . ", ". ").replace("..", ".").replace("-  - ", " - ").replace("  ", " ")])
                    return "- " + " - ".join([squished_rules_text.replace(". . ", ". ").replace("..", ".").replace("-  - ", " - ").replace("  ", " ")])
            except AttributeError:
                print card
                print sys.exc_info()
                return card + " " + str(sys.exc_info())
        else:
            message_out = ""
            message_out += ("*" if slackChannel else "") + card["name"] + ("* " if slackChannel else '\n')
            if(Names):
                message_out += "(Part of " + " // ".join(Names) + ")" + (" " if slackChannel else '\n')
            if(card["manaCost"]):
                message_out += card["manaCost"] + (" " if slackChannel else '\n')
                if not any(word in card["manaCost"] for word in "W U B R G") and Colors != []:
                    message_out += ", ".join(Colors) + (" " if slackChannel else '\n')
            else:
                message_out += ", ".join(Colors) + ("" if slackChannel else '\n')
            #print card["rarity"]
            message_out += ("|" if slackChannel else "") + " ".join(Supertypes) + (" " if Supertypes else "") + " ".join(Types) + (" - " if Subtypes else "") + " ".join(Subtypes)  + ("| " if slackChannel else '\n')
            if "Creature" in Types:
                message_out += card["power"] + "/" + card["toughness"] + (" " if slackChannel else '\n')
            if "Planeswalker" in Types:
                message_out += "[" + str(card["loyalty"]) + "]" + ("  " if slackChannel else '\n')
            if slackChannel:
                message_out += card["text"].encode('utf-8').replace('\n', ' / ')
            else:
                message_out += card["text"].encode('utf-8') + '\n'
        if extend and not slackChannel:
            message_out += "----------" + '\n'
            sources = c.execute('SELECT "set", source, rarity, starter, artist, flavor FROM cards WHERE name = ?', (card["name"],)).fetchall()
            for p in Printings:
                #print p
                setcode = c.execute('SELECT name FROM sets WHERE code = ?', (p,)).fetchone()
                #print setcode
                source = next(x for x in sources if x[0] == p)
                message_out += setcode[0] + " (" + source[2] + ((") (" + source[1] + ")") if source[1] else ")") + (" (Starter Pack)" if source[3] else "") + " [" + source[4] + "]" + '\n'
                if source[5]:
                    message_out += source[5] + '\n'
            message_out += "----------" + '\n'
            if extend > 0:
                #if card["originalText"] != "" and (card["originalText"] != card["text"]):
                #    message_out += "-----------\n" + '\n'
                #    message_out += card["originalText"] + '\n'
                #    message_out += card["originalType"] + '\n'
                #    message_out += "-----------\n" + '\n'
                if Rulings != []:
                    message_out += "----------" + '\n'
                    for rule in Rulings:
                        message_out += rule["text"] + "\n"
                    message_out += "----------\n"
                if Legalities != []:
                    for l in Legalities:
                        message_out += l["format"] + " : " + l["legality"] + '\n'

                dbForeignNames = c.execute('SELECT foreignNames FROM cards WHERE name = ?', (card["name"],)).fetchall()
                foreignNames = {}
                for dbNameList in dbForeignNames:
                    if dbNameList[0] != '[]':
                        nameList = ast.literal_eval(dbNameList[0])
                        for name in nameList:
                            foreignNames[name["language"]] = name["name"]

                for fPrint in foreignNames.items():
                    message_out += fPrint[0].encode("utf-8") + " : " + fPrint[1].encode("utf-8") + '\n'
        return message_out

    try:
      with open('CR.txt') as data_file:
        rules = data_file.readlines()
    except IOError:
      print "Unable to open Comprehensive Rules, r search will not be available"
      rules = []

    terms = {}
    all_rules = {}
    for rule in rules:
        x = rule.split('. ')
        all_rules[x[0]] = ". ".join(x[1:])

    # TODO
    # Difflib ratio
    # Foreign search
    # FRF boosters broken
    # DKA boosters broken
    # FUT boosters broken
    # Sealed pool generator

    # Rules parsing including examples

    # Try open the database
    try:
        conn = sqlite.connect('frytherer.db', check_same_thread=False)
        conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
        conn.row_factory = sqlite.Row
        c = conn.cursor()
    except sqlite.OperationalError:
        print "Unable to open database - goodbye"
        sys.exit(0)

    numCards = -1

    # Check if the database actually has stuff
    try:
        c.execute('SELECT COUNT(DISTINCT(name)) FROM cards')
        numCards = c.fetchone()[0]
    except sqlite.OperationalError:
        print "No cards in DB? Trying to import"
        numCards = 0

    if numCards < 1:
        # Load in all the cards
        try:
            with open('AllSets-x.json') as data_file:
                gatherer = json.load(data_file)
        except IOError:
            print "Unable to import cards - goodbye"
            sys.exit(0)
        c.execute("DROP TABLE IF EXISTS sets");
        c.execute("DROP TABLE IF EXISTS cards");
        c.execute("""
            CREATE TABLE sets (
                name TEXT PRIMARY KEY UNIQUE,
                code TEXT,
                languagesPrinted TEXT,
                releaseDate TEXT,
                type TEXT,
                magicCardsInfoCode TEXT,
                border TEXT,
                block TEXT,
                booster TEXT
                    )""")
        c.execute("""
            CREATE TABLE cards (
                name TEXT,
                names TEXT,
                printings TEXT,
                'set' TEXT,
                layout TEXT,
                artist TEXT,
                multiverseid NUMERIC,
                foreignNames TEXT,
                cmc NUMERIC,
                number TEXT,
                rarity TEXT,
                colors TEXT,
                imageName TEXT,
                text TEXT,
                originalText TEXT,
                manaCost TEXT,
                type TEXT,
                originalType TEXT,
                flavor TEXT,
                types TEXT,
                subtypes TEXT,
                supertypes TEXT,
                legalities TEXT,
                power TEXT,
                toughness TEXT,
                watermark TEXT,
                rulings TEXT,
                loyalty NUMERIC,
                source TEXT,
                starter TEXT
                    )""")

        for setname in gatherer.keys():
            s = gatherer[setname]
            c.execute("""
                INSERT INTO sets VALUES (
                    ?, ?, ?, ?, ?, ?, ?, ?, ?
                        )""", (s['name'].encode('utf-8'), s['code'].encode('utf-8'), str(s.get('languagesPrinted', [])), s.get('releaseDate', '').encode('utf-8'), s.get('type', '').encode('utf-8'), s.get('magicCardsInfoCode', '').encode('utf-8'), s['border'].encode('utf-8'), s.get('block', '').encode('utf-8'), str(s.get('booster', []))))

            for card in s['cards']:
                c.execute("""
                    INSERT INTO cards VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )""", (card['name'].replace(u"Æ", "Ae").replace(u"á", "a").encode('utf-8'), str(card.get('names', [])), str(card.get('printings', [])), s['code'].encode('utf-8'), card.get('layout', '').encode('utf-8'), card['artist'].encode('utf-8'), card.get('multiverseid', 0), str(card.get('foreignNames', [])), card.get('cmc', 0), card.get('number', '').encode('utf-8'), card['rarity'].encode('utf-8'), str(card.get('colors', [])), card['imageName'].encode('utf-8'), card.get('text', '').encode('utf-8'), card.get('originalText', '').encode('utf-8'), card.get('manaCost', '').encode('utf-8'), card['type'].encode('utf-8'), card.get('originalType', '').encode('utf-8'), card.get('flavor', '').encode('utf-8'), str(card.get('types', [])), str(card.get('subtypes', [])), str(card.get('supertypes', [])), str(card.get('legalities', [])), card.get('power', '').encode('utf-8'), card.get('toughness', '').encode('utf-8'), card.get('watermark', '').encode('utf-8'), str(card.get('rulings', [])), card.get('loyalty', 0), card.get('source', '').encode('utf-8'), str(card.get('starter', '')).encode('utf-8')))

        c.execute('CREATE INDEX cardindex ON cards (name)')
        c.execute('CREATE INDEX cardsetindex ON cards (\"set\")')
        c.execute('CREATE INDEX cardrarityindex ON cards (rarity)')
        c.execute('CREATE INDEX cardtypesindex ON cards (types)')
        conn.commit()
        del gatherer

    # Loads in a list of the cards in the holiday cube
    try:
        with open('holidaycube.txt') as cube_file:
            holidaycube_cards = cube_file.readlines()
    except IOError:
        print "Unable to import Holiday Cube list"
        holidaycube_cards = []

    try:
        with open('2015cubeupdate.txt') as cube_file:
            newcube_cards = cube_file.readlines()
    except IOError:
        print "Unable to import 2015 Cube list"
        newcube_cards = []

    try:
        with open('legendarycube.txt') as cube_file:
            legendarycube_cards = cube_file.readlines()
    except IOError:
        print "Unable to import Holiday Cube list"
        legendarycube_cards = []

    c.execute('SELECT DISTINCT(name) FROM cards')
    allCardNames = [x[0] for x in c.fetchall()]

    def helpsearch(message):
        message.reply("""
    All these options can be combined to more complicated queries: "a or b", "a not b", "a (b or c)", "a or (b c)", and so on.
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
    #     (new) in:wu (Any card that is white or blue according to the color indicator.)
    Mana Cost:
        mana=3G (Spells that cost exactly 3G, or split cards that can be cast with 3G)
        mana>=2WW (Spells that cost at least two white and two colorless mana)
        mana<GGGGGG (Spells that can be cast with strictly less than six green mana)
        mana>=2RR mana<=6RR (Spells that cost two red mana and between two and six colorless mana)
    #     (new) mana>={2/R}
    #     (new) mana>={W/U}
    #     (new) mana>={U/P}
        mana!{G}{G} (Spells whose mana cost contains {G}{G})
        mana!P (Spells whose mana cost contains Phyrexian mana)
    Power, Toughness, Converted Mana Cost:
        pow>=8
        tou<pow (All combinations are possible)
        cmc=7
    #     (new) cmc>=*
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
    #   is:old, is:new, is:future (Old/new/future card face)
        is:timeshifted
        is:funny, not:funny (Unglued/Unhinged/Happy Holidays Promos)
        is:promo (Promotional cards)
        is:promo is:old (Promotional cards with the original card face)
        (new) is:permanent, is:spell
    #   (new) is:black-bordered, is:white-bordered, is:silver-bordered
    """)

    def help(message):
        ret = ""
        ret += "Welcome to Frytherer.  Your options are:\n"
        ret += "\t<card name> - gives what's on the card\n"
        ret += "\t<card name> extend - gives extended info about the card (everything - rulings, legality, artist, flavour text, foreign names)\n"
        ret += "\t<card name>* - search card names\n"
        ret += "\tr <text> - search the comprehensive rules for text (allows for regexps)\n"
        ret += "\ts <text> - advanced search for cards with particular characteristics.  Type helpsearch for info\n"
        ret += "\t\tqs <text> - same as above but only give card names\n"
        ret += "\trandom - gives a random card\n"
        ret += "\tprintsets - gives a list of all the sets I know about\n"
        ret += "\tprintsetsinorder - gives a list of all the sets in release date order\n"
        #ret += "\tallcards <set> - gives a list of all the cards with a given set code (use printsets to get the code)\n"
        #ret += "\tallcardsextend <set> - gives the text of all the cards with a given set code (use printsets to get the code)\n"
        #ret += "\tbooster <set> - gives a randomly generated booster from either set code, or set name\n"
        #ret += "\tqbooster <set> - gives a randomly generated booster from either set code, or set name, short names\n"
        ret += "\thelp - prints this help\n"
        message.reply(ret)

# Message = ['__class__', '__delattr__', '__dict__', '__doc__',
#    '__format__', '__getattribute__', '__hash__', '__init__',
#    '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
#    __setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
#    '_body', '_client', '_gen_at_message', '_get_user_id', '_plugins', 'body',
#    'channel', 'docs_reply', 'gen_reply', 'react', 'reply', 'reply_webapi', 'send', 'send_webapi']



    @listen_to('^!(.*)')
    @respond_to('(.*)')
    def handle_message(message, card_name):
        if(card_name == "" or card_name == "\n"):
            return
        channel_message = False
        if(message.body['text'].startswith("!")):
            print "Channel Message!"
            print message.body
            # Command from a channel
            channel_message = True
            if(rule_regexp.match(card_name)):
                card_name = "r " + card_name
        cards = []
        y = []

        # Display extended information about a card
        extend = False
        # Search card text instead of name
        text = False
        # Do a regular expression search of the card name
        match = False
        # Search terms instead of name
        search = False
        # Print full matches
        quick = False

        if card_name.startswith("t "):
            text = True
            card_name = card_name[2:]
        elif card_name.endswith("extend"):
            extend = True
            card_name = card_name[:-6].rstrip()
        elif card_name.endswith("*"):
            match = True
            card_name = card_name[:-1]
        elif card_name.startswith("s ") or card_name.startswith("qs "):
            search = True
            if card_name.startswith("qs "):
                quick = True
                card_name = card_name[3:].lower()
            else:
                card_name = card_name[2:].lower()
            #output = ""
            output = []
            try:
                parsed_data = super_total.parseString(card_name)
            except ParseException:
                message.reply("Unable to parse search terms")
                return

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

            cards = new_filter_function(output)
        elif card_name == "random":
            # Pick a random card from all the cards
            card_name = random.choice(allCardNames)
        elif card_name.startswith("r "):
            if rules == []:
              message.reply("Rules search not available")
              return
            card_name = card_name[2:]
            if card_name in all_rules:
                message.reply(card_name + ": " + all_rules[card_name])
            else:
                rules_list = [(x, y) for (x, y) in all_rules.items() if re.search(card_name, y,  re.I)]
                for (rule_no, rule) in sorted(rules_list):
                    message.reply(str(rule_no) + ": " + rule)
            pass
        elif card_name == "printsets":
            # Print out the name of all the sets we know about
            c.execute('SELECT DISTINCT(name), code FROM sets ORDER BY name ASC')
            message_out = ""
            for name, code in [(x[0], x[1]) for x in c.fetchall()]:
                message_out += name + " (" + code + ")" + "\n"
            message.reply(message_out)
            return
        elif card_name == "printsetsinorder":
            c.execute('SELECT DISTINCT(name), code, releaseDate FROM sets ORDER BY releaseDate ASC')
            message_out = ""
            for name, code, date in [(x[0], x[1], x[2]) for x in c.fetchall()]:
                message_out += name + " (" + code + ")" + " [" + date + "]" + "\n"
            message.reply(message_out)
            return
        elif card_name == "help":
            help(message)
            pass
        elif card_name == "helpsearch":
            helpsearch(message)
            pass

        if text:
            cards = c.execute('SELECT * FROM cards WHERE text LIKE ? GROUP BY name', ('%' + card_name + '%',)).fetchall()
        elif match:
            cards = c.execute('SELECT * FROM cards WHERE name LIKE ? GROUP BY name', ('%' + card_name + '%',)).fetchall()
        elif not search:
            cards = c.execute('SELECT * FROM cards WHERE name = ? OR name = ? LIMIT 1', (card_name.strip(), gathererCapitalise(card_name.strip()),)).fetchall()

        if cards != []:
            message_out = ""
            for card in cards:
                message_out += printCard(card, quick=quick, extend=(2 if extend else 0), slackChannel=True)
            if not channel_message:
                message_out += (str(len(cards)) + " result/s")
            else:
                message_out = message_out.replace('\n', ' ')
            message.reply(message_out)

    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

    bot = Bot()
    print "Bot instantiated"
    bot.run()
