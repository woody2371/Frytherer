#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import json, re, rlcompleter, random, sys
from pyparsing import *
try:
     import readline
except ImportError:
     import pyreadline as readline
import signal, ast, string
from itertools import product
from operator import and_, or_
import pysqlite2.dbapi2 as sqlite

def gathererCapitalise(string):
    words = string.split(" ")
    ret_string = []
    for x in words:
        if x not in ["of", "in", "to", "and", "the"]:
            ret_string.append(x.title())
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

# [{u'legality': u'Legal', u'format': u'Commander'}, {u'legality': u'Legal', u'format': u'Freeform'}, {u'legality': u'Legal', u'format': u'Legacy'}, {u'legality': u'Legal', u'format': u'Modern'}, {u'legality': u'Legal', u'format': u'Prismatic'}, {u'legality': u'Legal', u'format': u'Singleton 100'}, {u'legality': u'Legal', u'format': u'Standard'}, {u'legality': u'Legal', u'format': u'Theros Block'}, {u'legality': u'Legal', u'format': u'Tribal Wars Legacy'}, {u'legality': u'Legal', u'format': u'Tribal Wars Standard'}, {u'legality': u'Legal', u'format': u'Vintage'}]

            if term.startswith("banned:"):
                sql_query += "legalities LIKE '%u''legality'': u''Banned'', u''format'': u''" + term[7:].title() + "''%'"
            elif term.startswith("legal:"):
                sql_query += "legalities LIKE '%u''legality'': u''Legal'', u''format'': u''" + term[6:].title() + "''%'"
            elif term.startswith("restricted:"):
                sql_query += "legalities LIKE '%u''legality'': u''Restricted'', u''format'': u''" + term[11:].title() + "''%'"
            elif term.startswith("set:"):
                sql_query += "(\"set\" = '" + term[4:] + "' OR printings LIKE '%" + term[4:].title() + "%')"
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
                    sql_query += "power" + term[3:].replace("pow", "power").replace("tou", "toughness")
            elif term.startswith("tou"):
                sql_query += "toughness" + term[3:].replace("pow", "power").replace("tou", "toughness").replace("cmc", "abs(cmc)")
            elif term.startswith("cmc"):
                sql_query += term.replace("pow", "power").replace("tou", "toughness")
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
                sql_query += op.join(query_term)
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
    colon_mode = oneOf("n o t in pow tou cmc r f a banned legal restricted is set")
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

    ctrlc = 0

    def signal_handler(signal, frame):
        global ctrlc
        if ctrlc == 1:
            conn.close()
            sys.exit(0)
        else:
            sys.stdout.write("\nPress Ctrl-C again to exit\n>: ")
            sys.stdout.flush()
            ctrlc = 1

    # Capture Ctrl-C (make them do it twice to exit)
    signal.signal(signal.SIGINT, signal_handler)

    def safe_list_get (l, idx, default):
        try:
            if l[idx] != None:
                return l[idx]
            else:
                return ""
        except IndexError:
            return default

    def printCard(card, extend=0, prepend="", quick=True, short=False, ret=False):
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
                    print prepend + card["name"] + " (" + card["manaCost"] + ")"
                else:
                    # Do some MODO-like compression of rules text to get it to fit
                    if not ret:
                        print prepend + card["name"],
                        if "/" in card["manaCost"]:
                            print "(" + card["manaCost"] + ")",
                        else:
                            print "(" + card["manaCost"].replace("{", "").replace("}", "") + ")",
                    squished_rules_text = " ".join([x[0] for x in Types])
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
                    print "- " + " - ".join([squished_rules_text.replace(". . ", ". ").replace("..", ".").replace("-  - ", " - ").replace("  ", " ")])
            except AttributeError:
                print card
                print sys.exc_info()
        else:
            print card["name"]
            if(Names):
                print "(Half of " + " // ".join(Names) + ")"
            if(card["manaCost"]):
                print card["manaCost"]
                if not any(word in card["manaCost"] for word in "W U B R G") and Colors != []:
                    print ", ".join(Colors)
            #print card["rarity"]
            print " ".join(Supertypes) + (" " if Supertypes else "") + " ".join(Types) + (" - " if Subtypes else "") + " ".join(Subtypes)
            if "Creature" in Types:
                print card["power"] + "/" + card["toughness"]
            if "Planeswalker" in Types:
                print "[" + str(card["loyalty"]) + "]"
            print card["text"].encode('utf-8')
        if extend:
            print "\n----------"
            sources = c.execute('SELECT "set", source, rarity FROM cards WHERE name = ?', (card["name"],)).fetchall()
            for p in Printings:
                #print p
                setcode = c.execute('SELECT name FROM sets WHERE code = ?', (p,)).fetchone()
                #print setcode
                source = next(x for x in sources if x[0] == p)
                print setcode[0] + " (" + source[2] + ((") (" + source[1] + ")") if source[1] else ")")
            print "\n----------"
            if extend > 0:
                if card["originalText"] != card["text"]:
                    print "-----------\n"
                    print card["originalText"]
                    print card["originalType"]
                    print "-----------\n"
                if Rulings != []:
                    print "\n----------"
                    for rule in Rulings:
                        print rule["text"] + "\n"
                    print "----------\n"
                if Legalities != []:
                    for l in Legalities:
                        print l["format"] + " : " + l["legality"]
            if extend > 1:
                print "\n" + card["flavor"]
                print "Artist: " + card["artist"] + "\n"

                dbForeignNames = c.execute('SELECT foreignNames FROM cards WHERE name = ?', (card["name"],)).fetchall()
                foreignNames = {}
                for dbNameList in dbForeignNames:
                    if dbNameList[0] != '[]':
                        nameList = ast.literal_eval(dbNameList[0])
                        for name in nameList:
                            foreignNames[name["language"]] = name["name"]

                for fPrint in foreignNames.items():
                    print fPrint[0].encode("utf-8") + " : " + fPrint[1].encode("utf-8")

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

    # Try open the database
    try:
        conn = sqlite.connect('frytherer.db')
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
                        )""", (s['name'].encode('utf-8'), s['code'].encode('utf-8'), str(s.get('languagesPrinted', [])), s['releaseDate'].encode('utf-8'), s['type'].encode('utf-8'), s.get('magicCardsInfoCode', '').encode('utf-8'), s['border'].encode('utf-8'), s.get('block', '').encode('utf-8'), str(s.get('booster', []))))

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

    # Let's make an array with the list of all the card names, to help tab completion
    c.execute('SELECT code, name FROM sets')
    allSets = {}
    for x in c.fetchall():
        allSets[x["code"]] = x["name"]
    print "Searching " + str(len(allSets)) + " sets"
    c.execute('SELECT DISTINCT(name) FROM cards')
    allCardNames = [x[0] for x in c.fetchall()]
    print "Searching " + str(len(allCardNames)) + " unique cards"

    def cardname_completer(text, state):
        options = [x for x in allCardNames if x.lower().startswith(text.lower())] + [x for x in ["help", "helpsearch", "random", "printsets", "printsetsinorder", "allcards", "allcardsextend", "booster", "exit"] if x.lower().startswith(text.lower())] + [None]
        if state < len(options):
            return options[state]
        else:
            return None

    # Activate tab complete
    try:
        if 'libedit' in readline.__doc__:
            print "Mac Tab Mode Active, your tab complete is going to be a bit shit! :(\n"
            readline.parse_and_bind("bind ^I rl_complete")
        else:
            readline.parse_and_bind("tab: complete")
    except TypeError:
            readline.parse_and_bind("tab: complete")

    readline.set_completer_delims('')
    readline.set_completer(cardname_completer)

    def helpsearch():
        print """
    All these options can be combined to more complicated queries: "a or b", "a not b", "a (b or c)", "a or (b c)", and so on.
    Options prepended with '#' are not yet implemented

    Name:
        n:Birds of Paradise
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
    #     is:old, is:new, is:future (Old/new/future card face)
        is:timeshifted
        is:funny, not:funny (Unglued/Unhinged/Happy Holidays Promos)
        is:promo (Promotional cards)
        is:promo is:old (Promotional cards with the original card face)
        (new) is:permanent, is:spell
    #     (new) is:black-bordered, is:white-bordered, is:silver-bordered
    """

    def help():
        print "Welcome to Frytherer.  Your options are:"
        print "\t<card name> - gives what's on the card (allows for tab complete)"
        print "\t<card name> extend - gives extended info about the card (everything - rulings, legality, artist, flavour text, foreign names)"
        print "\t<card name>* - search card names"
        print "\tt <text> - search rules text of cards"
        print "\tr <text> - search the comprehensive rules for text (allows for regexps)"
        print "\ts <text> - advanced search for cards with particular characteristics.  Type helpsearch for info"
        print "\t\tqs <text> - same as above but only give card names"
        print "\trandom - gives a random card"
        print "\tprintsets - gives a list of all the sets I know about"
        print "\tprintsetsinorder - gives a list of all the sets in release date order"
        print "\tallcards <set> - gives a list of all the cards with a given set code (use printsets to get the code)"
        print "\tallcardsextend <set> - gives the text of all the cards with a given set code (use printsets to get the code)"
        print "\tbooster <set> - gives a randomly generated booster from either set code, or set name"
        print "\t\tbooster holidaycube <number> - gives an amount of randomly generated boosters from the MTGO Holiday Cube"
        print "\t\tbooster cube2015 <number> - gives an amount of randomly generated boosters from the MTGO 2015 Cube"
        print "\thelp - prints this help"
        print "\texit - goodbye :("

    # Print the help information initially
    help()

    while(1):
        card_name = raw_input(">: ")
        ctrlc = 0
        if(card_name == "" or card_name == "\n"):
            continue
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
                print "Unable to parse search terms"
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

            cards = new_filter_function(output)
        elif card_name == "random":
            # Pick a random card from all the cards
            card_name = random.choice(allCardNames)
        elif card_name.startswith("r "):
            if rules == []:
              print "Rules search not available"
              continue
            card_name = card_name[2:]
            if card_name in all_rules:
                print card_name + ": " + all_rules[card_name]
            else:
                rules_list = [(x, y) for (x, y) in all_rules.items() if re.search(card_name, y,  re.I)]
                for (rule_no, rule) in sorted(rules_list):
                    print str(rule_no) + ": " + rule
            pass
        elif card_name == "printsets":
            # Print out the name of all the sets we know about
            c.execute('SELECT DISTINCT(name), code FROM sets ORDER BY name ASC')
            for name, code in [(x[0], x[1]) for x in c.fetchall()]:
                print name + " (" + code + ")"
            continue
        elif card_name == "printsetsinorder":
            c.execute('SELECT DISTINCT(name), code FROM sets ORDER BY releaseDate ASC')
            for name, code in [(x[0], x[1]) for x in c.fetchall()]:
                print name + " (" + code + ")"
            continue
        elif card_name.startswith("allcards"):
            # Print out all the cards in a given set
            if card_name.rstrip() == "allcards":
                continue
            set_name = card_name[9:].upper()
            # Try and look up the set name
            if set_name not in allSets.keys():
                setname = next((code for code, name in allSets.items() if name.lower() == set_name.lower()), None)
                if setname != None:
                    set_name = setname                
            try:
                i = 0
                cardlist = c.execute('SELECT * FROM cards WHERE "set" = ? GROUP BY name', (set_name,))
                for card in c.fetchall():
                    printCard(card, quick=(0 if card_name.startswith("allcardsextend") else 1), extend=(1 if card_name.startswith("allcardsextend") else 0))
                    i += 1
                print "\n" + str(i) + " result/s"
            except KeyError:
                print "Set not found"
            pass
        elif card_name.startswith("booster") or card_name.startswith("sealedpool"):
            if card_name.startswith("booster"):
                numboosters = 1
            else:
                numboosters = 6
                sealedpool = []
            if numboosters == 1:
                set_name = card_name[8:]
            else:
                set_name = card_name[11:]
            booster = None
            already_picked = []
            if set_name.upper() in allSets.keys():
                # They've kindly given us the three letter set code
                booster = ast.literal_eval(c.execute('SELECT booster FROM sets WHERE code = ?', (set_name.upper(),)).fetchone()[0])
                set_name = set_name.lower()
            elif set_name.lower().startswith("holidaycube") or set_name.lower().startswith("cube2015"):
                if set_name.lower().startswith("holidaycube"):
                    if holidaycube_cards == []:
                        print "Holiday Cube not loaded"
                        continue
                    else:
                        cube_cards = holidaycube_cards
                else:
                    if newcube_cards == []:
                        print "2015 Cube not loaded"
                        continue
                    else:
                        cube_cards = newcube_cards
                # Try and figure out how many boosters they want
                # If we can't, just give them one
                number = set_name.split(" ", 2)
                try:
                    number = int(number[1])
                except ValueError:
                    number = 1
                except IndexError:
                    number = 1
                newcube = cube_cards[:]
                random.shuffle(newcube)
                for j in xrange(number):
                    print "Booster # " + str(j)
                    cubebooster = []
                    if len(newcube) < 15:
                        print "Run out of cards in the cube!"
                        break
                    for i in xrange(15):
                        cubebooster.append(newcube.pop())
                    for card in cubebooster:
                        if "&" in card:
                            card = card.split(" & ")[0]
                            print card
                            sys.exit(1)
                        try:
                            y = c.execute('SELECT * FROM cards WHERE name = ? LIMIT 1', (card.rstrip(),)).fetchall()[0]
                        except IndexError:
                            print "Unable to fetch card " + card.rstrip()
                        printCard(y, quick=True, short=True)
                    print "-------\n"
                continue
            # They've probably given us the english name, let's try and find it
            else:
                setname = next((code for code, name in allSets.items() if name.lower() == set_name.lower()), None)
                if setname != None:
                    booster = c.execute('SELECT booster FROM sets WHERE code = ?', (str(setname),)).fetchone()[0]
                    if booster != None:
                        booster = ast.literal_eval(str(booster))
                    set_name = setname.lower()
                else:
                    print "Couldn't understand what set you wanted"
                    continue
            if booster != None and booster != []:
                for i in xrange(numboosters):
                    if set_name != "vma" and set_name != "mma" and set_name != "mm2":
                        # 25% chance of having a foil
                        isFoil = (random.randint(1, 4) == 1)
                        if isFoil:
                            newbooster = booster[:]
                            # Replace a common with a foil
                            if set_name == "fut":
                                newbooster[-1] = "foil"
                            else:
                                newbooster[len(booster) - booster[::-1].index("common") - 1] = "foil"
                            booster = newbooster
                    for rarity in booster:
                        if type(rarity) is list:
                            if len(rarity) == 2 and ("rare" in rarity) and ("mythic rare" in rarity):
                                # 7 : 1 chance of a mythic in a booster
                                weighted_choices = [('rare', 7), ('mythic rare', 1)]
                                population = [val for val, cnt in weighted_choices for i in range(cnt)]
                                rarity = random.choice(population)
                            elif len(rarity) == 2 and set_name == "vma":
                                # One in 53 chance of power 9
                                weighted_choices = [('foil', 52), ('power nine', 1)]
                                population = [val for val, cnt in weighted_choices for i in range(cnt)]
                                rarity = random.choice(population)
                            elif len(rarity) == 4 and set_name == "mma" or set_name == "mm2":
                                weighted_choices = [('foil mythic rare', 1), ('foil rare', 5), ('foil uncommon', 12), ('foil common', 18)]
                                population = [val for val, cnt in weighted_choices for i in range(cnt)]
                                rarity = random.choice(population)
                            elif len(rarity) == 2 and set_name == "isd":
                                rarity = "land"
                            elif len(rarity) == 2 and set_name == "fut":
                                rarity = rarity[0]
                            else:
                                print "Weird list of rarities: " + str(rarity)
                                rarity = rarity[0]
                        if rarity == "land":
                            if set_name == "frf":
                                card = c.execute('SELECT * FROM cards WHERE "set" = ? AND types LIKE \'%Land%\' AND name NOT IN (' + ",".join(['"' + x + '"' for x in already_picked]) + ') ORDER BY RANDOM() LIMIT 1', (set_name.upper(),)).fetchone()
                                if numboosters > 1:
                                    sealedpool.append(card)
                                else:
                                    printCard(card, prepend="L: ", short=True)
                            elif set_name == "dgm":
                                card = c.execute('SELECT * FROM cards WHERE "set" = ? AND types LIKE \'%Land%\'', (set_name.upper(),)).fetchone()
                                if numboosters > 1:
                                    sealedpool.append(card)
                                else:
                                    printCard(card, prepend="L: ", short=True)
                            elif set_name == "bfz":
                                weighted_choices = [('land', 259), ('expedition', 1)]
                                population = [val for val, cnt in weighted_choices for i in range(cnt)]
                                rarity = random.choice(population)
                                if rarity == "land":
                                    if numboosters > 1:
                                        sealedpool.append(card)
                                    else:
                                        print "L: " + random.choice(["Plains", "Island", "Swamp", "Mountain", "Forest"])
                                else:
                                    card = c.execute('SELECT * FROM cards WHERE "set" = \'EXP\' ORDER BY RANDOM() LIMIT 1').fetchone()
                                    if numboosters > 1:
                                        sealedpool.append(card)
                                    else:
                                        printCard(card, prepend="EXP: ", short=True)
                            else:
                                if numboosters > 1:
                                    sealedpool.append(random.choice(["Plains", "Island", "Swamp", "Mountain", "Forest"]))
                                else:
                                    print "L: " + random.choice(["Plains", "Island", "Swamp", "Mountain", "Forest"])
                            continue
                        elif rarity == "foil" and set_name == "vma":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND name NOT IN ("Black Lotus", "Timetwister", "Ancestral Recall", "Mox Ruby", "Mox Jet", "Mox Emerald", "Mox Sapphire", "Mox Pearl", "Time Walk") ORDER BY RANDOM() LIMIT 1', (set_name.upper(),)).fetchone()
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="Foil ", short=True)
                            continue
                        elif rarity == "foil":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? ORDER BY RANDOM() LIMIT 1', (set_name.upper(),)).fetchone()
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="Foil " + card["rarity"][0].upper() + ": ", short=True)
                            continue
                        elif rarity == "draft-matters":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND types LIKE \'%Conspiracy%\' ORDER BY RANDOM() LIMIT 1', (set_name.upper(),)).fetchone()
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="Conspiracy (" + card["rarity"][0].upper() + "): ", short=True)
                            continue
                        elif rarity == "marketing":
                            continue
                        elif rarity == "power nine":
                            card = ('SELECT * FROM cards WHERE set = ? AND name IN ("Black Lotus", "Timetwister", "Ancestral Recall", "Mox Ruby", "Mox Jet", "Mox Emerald", "Mox Sapphire", "Mox Pearl", "Time Walk") ORDER BY RANDOM() LIMIT 1', (set_name.upper(),)).fetchone()
                            # One in 28 chance of power 9 turning into foil power 9!
                            weighted_choices = [('', 27), ('Foil ', 1)]
                            population = [val for val, cnt in weighted_choices for i in range(cnt)]
                            extra = random.choice(population)
                            if numboosters > 1:
                                sealedpool.append(extra + "Power 9! : " + card["name"] + " (" + card["manaCost"] + ")")
                            else:                            
                                print extra + "Power 9! : " + card["name"] + " (" + card["manaCost"] + ")"
                            continue
                        elif rarity.startswith("foil") and (set_name == "mma" or set_name == "mm2"):
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND rarity = ? ORDER BY RANDOM() LIMIT 1', (set_name.upper(), rarity[5:].title())).fetchall()[0]
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="Foil ", short=True)
                            continue
                        elif rarity == "double faced":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND layout = ? AND cmc != ? ORDER BY RANDOM() LIMIT 1', (set_name.upper(), "double-faced", 0)).fetchall()[0]
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="D: ", short=True)
                            continue
                        elif rarity == "urza land":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND subtypes LIKE \'%Urza%\' AND name NOT IN (' + ",".join(['"' + x + '"' for x in already_picked]) + ') ORDER BY RANDOM() LIMIT 1', (set_name.upper(),)).fetchone()
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="UL: ", short=True)
                            continue
                        elif rarity == "timeshifted purple":
                            card = c.execute('SELECT * FROM cards WHERE "set" = "TSB" ORDER BY RANDOM() LIMIT 1').fetchall()[0]
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend="TS: ", short=True)
                            continue

                        if set_name == "isd":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND rarity = ? AND layout = \'normal\' AND name NOT IN (' + ",".join(['"' + x + '"' for x in already_picked]) + ') ORDER BY RANDOM() LIMIT 1', (set_name.upper(), rarity.title())).fetchone()
                        elif (set_name == "frf" or set_name == "dgm") and rarity == "common":
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND rarity = ? AND types NOT LIKE \'%Land%\' AND name NOT IN (' + ",".join(['"' + x + '"' for x in already_picked]) + ') ORDER BY RANDOM() LIMIT 1', (set_name.upper(), rarity.title())).fetchone()
                        else:
                            #print ('SELECT * FROM cards WHERE \"set\" = %s AND starter != \'True\' AND rarity = %s AND types != %s AND name NOT IN ('  % (set_name.upper(), rarity.title(), 'u[\'Conspiracy\']')) + ",".join(['"' + x + '"' for x in already_picked]) + ') ORDER BY RANDOM() LIMIT 1'
                            card = c.execute('SELECT * FROM cards WHERE "set" = ? AND starter != \'True\' AND rarity = ? AND types != ? AND name NOT IN (' + ",".join(['"' + x + '"' for x in already_picked]) + ') ORDER BY RANDOM() LIMIT 1', (set_name.upper(), rarity.title(), 'u[\'Conspiracy\']')).fetchone()

                        if card != None:
                            if numboosters > 1:
                                sealedpool.append(card)
                            else:
                                printCard(card, prepend=rarity[0].upper() + ": ", short=True)
                            already_picked.append(card["name"])

                if numboosters > 1:
                    sealed_text = []
                    for card in sealedpool:
                        sealed_text.append(printCard(card, short=True, ret=True))
                    for card in sorted(sealed_text):
                        print card
                    sealedpool = []
                    sealed_text = []
            else:
                print "It doesn't appear this set came in boosters\n"
            pass
        elif card_name == "help":
            help()
            pass
        elif card_name == "helpsearch":
            helpsearch()
            pass
        elif card_name == "exit":
            conn.close()
            sys.exit(0)

        if text:
            cards = c.execute('SELECT * FROM cards WHERE text LIKE ? GROUP BY name', ('%' + card_name + '%',)).fetchall()
        elif match:
            cards = c.execute('SELECT * FROM cards WHERE name LIKE ? GROUP BY name', ('%' + card_name + '%',)).fetchall()
        elif not search:
            cards = c.execute('SELECT * FROM cards WHERE name = ? OR name = ? LIMIT 1', (card_name.strip().replace(u"Æ", "Ae"), gathererCapitalise(card_name.strip().replace(u"Æ", "Ae")),)).fetchall()

        if cards != []:
            for card in cards:
                printCard(card, quick=quick, extend=(2 if extend else 0))
                if not quick:
                    print "\n"
            print str(len(cards)) + " result/s"
