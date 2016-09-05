"""Frytherer Module.

This module contains all the helper functions for the
Frytherer command line interface and the Slackbot
"""
import string, sys, ast
from itertools import product
from operator import and_, or_
try:
    import re2 as re
except ImportError:
    import re
import logging
logging.basicConfig(level=logging.DEBUG)

mana_regexp = re.compile('([0-9]*)(b*)(g*)(r*)(u*)(w*)')
section_regexp = re.compile('(aipg|amtr) (?:(appendix [a-f])|(\d+)(?:(?:\.)(\d)){0,1})')


def gathererCapitalise(y):
    """
    Capitalise card names as Gatherer does.

    INPUT: Regular card name in whatever case
    OUTPUT: Magic style capitalised card name
    """
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
            elif term.startswith("en:"):
                sql_query += "name LIKE '" + term[3:].replace('"', '') + "'"
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
    logging.debug(sql_query)
    cards = cursor.execute(sql_query).fetchall()
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
            message_out += card["text"].encode('utf-8').replace('\n', ' / ')
        else:
            message_out += card["text"].encode('utf-8') + '\n'
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
                message_out += fPrint[0].encode("utf-8") + " : " + fPrint[1].encode("utf-8") + '\n'
    return message_out


def ruleSearch(all_rules, rule_to_search):
    """Search the rules of the game.

    INPUT: A rule number, or text
    OUTPUT: The rule number and text of the matching rule
    """
    if all_rules == {}:
        return "Rules search not available"
    if rule_to_search in all_rules:
        return (rule_to_search + ": " + all_rules[rule_to_search])
    else:
        rules_list = [(x, y) for (x, y) in all_rules.items() if re.search(rule_to_search, y, re.I)]
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
    ret += "url <cr|mtr|amtr (<section>)|ipg|aipg (<section>|<infraction>)|jar|peip|pptq|rptq|alldocs> - gives the URL to the requested document"
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
    ret = ""
    if document == "mtr":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_mtr_22jul16_en.pdf"
    elif document == "ipg":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_ipg_22jul16_en.pdf"
    elif document == "jar":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_jar_4.pdf"
    elif document == "peip":
        ret = "http://wpn.wizards.com/sites/wpn/files/attachements/mtg_peip-16_16feb8_en.pdf"
    elif document == "cr":
        ret = "http://yawgatog.com/resources/magic-rules/"
    elif document == "alldocs":
        ret = "http://wpn.wizards.com/en/resources/rules-documents"
    elif document == "pptq":
        ret = "http://magic.wizards.com/en/events/instoreplay/pptqaer"
    elif document == "rptq":
        ret = "http://magic.wizards.com/en/events/instoreplay/rptqaer"
    elif document == "aipg":
        ret = "http://blogs.magicjudges.org/rules/ipg/"
    elif document == "amtr":
        ret = "http://blogs.magicjudges.org/rules/mtr/"
    elif document == "mt" or document == "missed trigger":
        ret = "http://blogs.magicjudges.org/rules/ipg2-1/"
    elif document == "l@ec" or document == "lec" or document == "looking at extra cards":
        ret = "http://blogs.magicjudges.org/rules/ipg2-2/"
    elif document == "hce" or document == "hidden card error":
        ret = "http://blogs.magicjudges.org/rules/ipg2-3/"
    elif document == "mpe" or document == "mulligan procedure error":
        ret = "http://blogs.magicjudges.org/rules/ipg2-4/"
    elif document == "grv" or document == "game rule violation":
        ret = "http://blogs.magicjudges.org/rules/ipg2-5/"
    elif document == "ftmgs" or document == "failure to maintain game state":
        ret = "http://blogs.magicjudges.org/rules/ipg2-6/"
    elif document == "tardiness":
        ret = "http://blogs.magicjudges.org/rules/ipg3-1/"
    elif document == "oa" or document == "outside assistance":
        ret = "http://blogs.magicjudges.org/rules/ipg3-2/"
    elif document == "slow play":
        ret = "http://blogs.magicjudges.org/rules/ipg3-3/"
    elif document == "insufficient shuffling":
        ret = "http://blogs.magicjudges.org/rules/ipg3-4/"
    elif document == "ddlp" or document == "d/dlp" or ("deck" in document and "problem" in document):
        ret = "http://blogs.magicjudges.org/rules/ipg3-5/"
    elif document == "lpv" or document == "limited procedure violation":
        ret = "http://blogs.magicjudges.org/rules/ipg3-6/"
    elif document == "cpv" or document == "communication policy violation":
        ret = "http://blogs.magicjudges.org/rules/ipg3-7/"
    elif document == "mc" or document == "marked cards":
        ret = "http://blogs.magicjudges.org/rules/ipg3-8/"
    elif document.startswith("usc") or "unsporting conduct" in document:
        if "mi" in document:
            ret = "http://blogs.magicjudges.org/rules/ipg4-1/"
        elif "ma" in document:
            ret = "http://blogs.magicjudges.org/rules/ipg4-2/"
    elif document == "idaw" or document == "improperly determining a winner":
        ret = "http://blogs.magicjudges.org/rules/ipg4-3/"
    elif document == "b&w" or "bribery" in document:
        ret = "http://blogs.magicjudges.org/rules/ipg4-4/"
    elif document == "ab" or "aggressive" in document:
        ret = "http://blogs.magicjudges.org/rules/ipg4-5/"
    elif document == "totm" or "theft" in document:
        ret = "http://blogs.magicjudges.org/rules/ipg4-6/"
    elif document == "stalling":
        ret = "http://blogs.magicjudges.org/rules/ipg4-7/"
    elif document == "cheating":
        ret = "http://blogs.magicjudges.org/rules/ipg4-8/"
    elif section_regexp.match(document):
        try:
            (doco, appendix, main, sub) = (section_regexp.match(document)).groups()
            if doco == "aipg":
                if appendix:
                    (app, letter) = appendix.split(" ")
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
                            ret = "http://blogs.magicjudges.org/rules/ipg%d-%d" % (main, sub)
                        else:
                            ret = "Invalid section requested"
                else:
                    ret = "Invalid section requested"
            elif doco == "amtr":
                if appendix:
                    (app, letter) = appendix.split(" ")
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
                            ret = "http://blogs.magicjudges.org/rules/mtr%d-%d" % (main, sub)
                        else:
                            ret = "Invalid section requested"
                else:
                    ret = "Invalid section requested"
            else:
                ret = "Something went wrong parsing your request"
        except:  # pragma: no cover
            logging.debug(sys.exc_info())
            ret = "Something went wrong parsing your request"
    else:
        ret = "I didn't understand what document you wanted"
    return ret
