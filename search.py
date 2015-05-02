#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import json
#import difflib
from pyparsing import *
import multiprocessing
from functools import partial
import re
import sre_constants
try:
     import readline
except ImportError:
     import pyreadline as readline
import rlcompleter
import random
import sys
import signal
from itertools import product
from operator import and_, or_

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

# define classes to be built at parse time, as each matching
# expression type is parsed
class BoolOperand(object):
    def __init__(self,t):
        self.label = t[0]
        self.value = eval(t[0])
    def __bool__(self):
        return self.value
    def __str__(self):
        return self.label
    __repr__ = __str__
    __nonzero__ = __bool__

class BoolBinOp(object):
    def __init__(self,t):
        self.args = t[0][0::2]
    def __str__(self):
        sep = " %s " % self.reprsymbol
        return "(" + sep.join(map(str,self.args)) + ")"
    def __bool__(self):
        return self.evalop(bool(a) for a in self.args)
    __nonzero__ = __bool__
    __repr__ = __str__

class BoolAnd(BoolBinOp):
    reprsymbol = '&'
    evalop = all

class BoolOr(BoolBinOp):
    reprsymbol = '|'
    evalop = any

class BoolNot(object):
    def __init__(self,t):
        self.arg = t[0][1]
    def __bool__(self):
        v = bool(self.arg)
        return not v
    def __str__(self):
        return "~" + str(self.arg)
    __repr__ = __str__
    __nonzero__ = __bool__

TRUE = Keyword("True")
FALSE = Keyword("False")
boolOperand = TRUE | FALSE | Word(alphas,max=1)
boolOperand.setParseAction(BoolOperand)

# define expression, based on expression operand and
# list of operations in precedence order
boolExpr = infixNotation( boolOperand,
    [
    ("not", 1, opAssoc.RIGHT, BoolNot),
    ("and", 2, opAssoc.LEFT,  BoolAnd),
    ("or",  2, opAssoc.LEFT,  BoolOr),
    ])

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
    input_array = re.split('([0-9]*)(b*)(g*)(r*)(u*)(w*)', input_string)

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
        print sys.exc_info()
    return cmc

# Used to take a card and search terms and a format string
# Compares card against search times, evaluates results in order
# against the format string

def filter_function(card, terms, output):
    returnBools = []
    values = {}

    values["pow"] = card.get("power", None)
    values["tou"] = card.get("toughness", None)
    values["cmc"] = card.get("cmc", None)
    values["mana"] = card.get("manaCost", None)
    values["legalities"] = card.get("legalities", [])
    values["layout"] = card.get("layout", "")
    types = " ".join(card.get("supertypes", [])) + (" " if card.get("supertypes", []) else "") + " ".join(card.get("types", [])) + " ".join(card.get("subtypes", []))
    if type(card.get("printings")) is list:
        values["printings_string"] = " ".join(card.get("printings"))
    else:
        values["printings_string"] = card.get("printings")

    for idx, term in enumerate(terms):
        ret = False

        if term.startswith("banned:"):
            if values["legalities"] != [] and values["legalities"].get(term[7:].title(), "") == "Banned":
                ret = True
        elif term.startswith("legal:"):
            if values["legalities"] != [] and values["legalities"].get(term[6:].title(), "") == "Legal":
                ret = True
        elif term.startswith("restricted:"):
            if values["legalities"] != [] and values["legalities"].get(term[11:].title(), "") == "Restricted":
                ret = True
        elif term.startswith("pow"):
            # Quick shortcut for things that don't have power
            if values["pow"] == None:
                returnBools.append(False)
                continue
            try:
                if term[3:].startswith(">="):
                    if term[5:] in values:
                        if int(values["pow"]) >= int(values[term[5:]]):
                            ret = True
                    else:
                        if int(values["pow"]) >= int(term[5:]):
                            returnBools.append(True)
                            continue
                elif term[3:].startswith("<="):
                    if term[5:] in values:
                        if int(values["pow"]) <= int(values[term[5:]]):
                            ret = True
                        else:
                            if int(values["pow"]) <= int(term[5:]):
                                ret = True
                elif term[3] == ">":
                    if term[4:] in values:
                        if int(values["pow"]) > int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["pow"]) > int(term[4:]):
                            ret = True
                elif term[3] == "<":
                    if term[4:] in values:
                        if int(values["pow"]) < int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["pow"]) < int(values[term[4:]]):
                            ret = True
                elif term[3] == "=":
                    if term[4:] in values:
                        if int(values["pow"]) ==  int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["pow"]) == int(term[4:]):
                            ret = True
            except ValueError:
                #print "Unable to parse power value"
                returnBools.append(False)
                continue
            except TypeError:
                returnBools.append(False)
                continue
        elif term.startswith("tou"):
            # Quick shortcut for things that don't have toughness
            if values["tou"] == None:
                returnBools.append(False)
                continue
            try:
                if term[3:].startswith(">="):
                    if term[5:] in values:
                        if int(values["tou"]) >= int(values[term[5:]]):
                            ret = True
                    else:
                        if int(values["tou"]) >= int(term[5:]):
                            returnBools.append(True)
                            continue
                elif term[3:].startswith("<="):
                    if term[5:] in values:
                        if int(values["tou"]) <= int(values[term[5:]]):
                            ret = True
                        else:
                            if int(values["tou"]) <= int(term[5:]):
                                ret = True
                elif term[3] == ">":
                    if term[4:] in values:
                        if int(values["tou"]) > int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["tou"]) > int(term[4:]):
                            ret = True
                elif term[3] == "<":
                    if term[4:] in values:
                        if int(values["tou"]) < int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["tou"]) < int(values[term[4:]]):
                            ret = True
                elif term[3] == "=":
                    if term[4:] in values:
                        if int(values["tou"]) ==  int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["tou"]) == int(term[4:]):
                            ret = True
            except ValueError:
                #print "Unable to parse toughness value"
                returnBools.append(False)
                continue
            except TypeError:
                returnBools.append(False)
                continue
        elif term.startswith("cmc"):
            try:
                if term[3:].startswith(">="):
                    if term[5:] in values:
                        if int(values["cmc"]) >= int(values[term[5:]]):
                            ret = True
                    else:
                        if int(values["cmc"]) >= int(term[5:]):
                            returnBools.append(True)
                            continue
                elif term[3:].startswith("<="):
                    if term[5:] in values:
                        if int(values["cmc"]) <= int(values[term[5:]]):
                            ret = True
                        else:
                            if int(values["cmc"]) <= int(term[5:]):
                                ret = True
                elif term[3] == ">":
                    if term[4:] in values:
                        if int(values["cmc"]) > int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["cmc"]) > int(term[4:]):
                            ret = True
                elif term[3] == "<":
                    if term[4:] in values:
                        if int(values["cmc"]) < int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["cmc"]) < int(values[term[4:]]):
                            ret = True
                elif term[3] == "=":
                    if term[4:] in values:
                        if int(values["cmc"]) ==  int(values[term[4:]]):
                            ret = True
                    else:
                        if int(values["cmc"]) == int(term[4:]):
                            ret = True
            except ValueError:
                #print "Unable to parse CMC value"
                returnBools.append(False)
                continue
            except TypeError:
                returnBools.append(False)
                continue
        elif term.startswith("mana"):
            rets = []
            if values["mana"] == None:
                returnBools.append(False)
                continue
            if term[4] == "=":
                if values["mana"].replace("{", "").replace("}", "").lower() == term[5:].replace("{", "").replace("}", ""):
                    ret = True
            elif term[4] == "!":
                if re.search("".join(sorted(term[5:].replace("{", "").replace("}", "").lower())), "".join(sorted(values["mana"].replace("{", "").replace("}", "").lower())), re.I):
                    ret = True
            else:
                try:
                    mana_costs = calculateManaPerms(values["mana"].replace("W/P", "W").replace("U/P", "U").replace("B/P", "B").replace("R/P", "R").replace("G/P", "G"))
                    if term[4:].startswith(">="):
                        input_string = "".join(sorted(term[6:].replace("{", "").replace("}", "").lower()))
                        input_array = re.split('([0-9]*)(b*)(g*)(r*)(u*)(w*)', input_string)
                        manarets = []
                        for manacost in mana_costs:
                            rets = []
                            mana_cost_string = "".join(sorted(manacost.replace("X", "0").lower()))
                            mana_cost_array = re.split('([0-9]*)(b*)(g*)(r*)(u*)(w*)', mana_cost_string)
                            try:
                                for idx, term in enumerate(mana_cost_array):
                                    if idx != 0 and idx != len(mana_cost_array)-1:
                                        if term >= input_array[idx]:
                                            rets.append(True)
                                        else:
                                            rets.append(False)

                                ret = reduce(and_, rets)
                                manarets.append(ret)
                            except IndexError:
                                print card.get("name")
                        manarets = reduce(or_, manarets)
                        cmcret = None

                        # Calculate CMC of input string
                        cmc = calculateCMC(input_string)

                        # See if card only has generic mana
                        if len(card.get("colors", [])) == 0:
                            # If so, compare CMC of card to CMC of input string
                            if int(values["cmc"]) >= int(cmc):
                                cmcret = True
                            else:
                                cmcret = False
                        else:
                            cmcret = False

                        ret = cmcret or manarets
                        returnBools.append(ret)
                        continue
                    elif term[4:].startswith("<="):
                        input_string = "".join(sorted(term[6:].replace("{", "").replace("}", "").lower()))
                        input_array = re.split('([0-9]*)(b*)(g*)(r*)(u*)(w*)', input_string)
                        manarets = []
                        for manacost in mana_costs:
                            rets = []
                            mana_cost_string = "".join(sorted(manacost.replace("X", "0").lower()))
                            mana_cost_array = re.split('([0-9]*)(b*)(g*)(r*)(u*)(w*)', mana_cost_string)
                            try:
                                for idx, term in enumerate(mana_cost_array):
                                    if idx != 0 and idx != len(mana_cost_array)-1:
                                        if term <= input_array[idx]:
                                            rets.append(True)
                                        else:
                                            rets.append(False)
                                ret = reduce(and_, rets)
                                manarets.append(ret)
                            except IndexError:
                                print card.get("name")
                        manarets = reduce(or_, manarets)
                        cmcret = None

                        # Calculate CMC of input string
                        cmc = calculateCMC(input_string)

                        # See if card only has generic mana
                        if len(card.get("colors", [])) == 0:
                            # If so, compare CMC of card to CMC of input string
                            if int(values["cmc"]) <= int(cmc):
                                cmcret = True
                            else:
                                cmcret = False
                        else:
                            cmcret = False

                        ret = cmcret or manarets
                        returnBools.append(ret)
                        continue
                    elif term[4] == ">":
                        print "Inequality operators not yet implemented"
                        returnBools.append(False)
                        continue
                    elif term[4] == "<":
                        print "Inequality operators not yet implemented"
                        returnBools.append(False)
                        continue
                except ValueError:
                    returnBools.append(False)
                    continue
                except TypeError:
                    returnBools.append(False)
                    continue
        elif term.startswith("n:"):
            if re.search(term[2:].replace('"', ''), card.get("name", ""), re.I):
                ret = True
        elif term.startswith("t:"):
            if re.search(term[2:].replace('"', '').replace(' ', '.*'), types, re.I):
                ret = True
        elif term.startswith("r:"):
            if re.search(term[2:].replace('"', ""), card.get("rarity", ""), re.I):
                ret = True
        elif term.startswith("f:"):
            if values["legalities"] != [] and values["legalities"].get(term[2:].title(), "") == "Legal":
                ret = True
        elif term.startswith("a:"):
            if re.search(term[2:].replace('"', ""), card.get("artist", ""), re.I):
                ret = True
        elif term.startswith("is:"):
            # normal, split, flip, double-faced, token, plane, scheme, phenomenon, leveler, vanguard
            if term[3:] == "split":
                if values["layout"] == "split":
                    ret = True
            elif term[3:] == "flip":
                if values["layout"] == "flip":
                    ret = True
            elif term[3:] == "vanilla":
                if card.get("text", "") == "" and "Creature" in types:
                    ret = True
            elif term[3:] == "timeshifted":
                if card.get("rarity", "") == "Special" and "Timeshifted" in values["printings_string"]:
                    ret = True
            elif term[3:] == "funny":
                if "Happy Holidays" in values["printings_string"] or "Unglued" in values["printings_string"] or "Unhinged" in values["printings_string"]:
                    ret = True
            elif term[3:] == "promo":
                if card.get("source", "") != "" and "Theme" not in card.get("source"):
                    ret = True
            elif term[3:] == "permanent":
                if "Creature" in types or "Artifact" in types or "Enchantment" in types or "Planeswalker" in types or "Land" in types:
                    ret = True
            elif term[3:] == "spell":
                if "Sorcery" in types or "Instant" in types:
                    ret = True
        elif term.startswith("c"):
            rets = []
            for y in term[2:]:
                if y == 'w':
                    if 'White' in card.get("colors", []):
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'u':
                    if 'Blue' in card.get("colors", []):
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'b':
                    if 'Black' in card.get("colors", []):
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'r':
                    if 'Red' in card.get("colors", []):
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'g':
                    if 'Green' in card.get("colors", []):
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'm':
                    if len(card.get("colors", [])) > 1:
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'l':
                    if 'Land' in card.get("types", []):
                        rets.append(True)
                    else:
                        rets.append(False)
                if y == 'c':
                    if len(card.get("colors", [])) == 0:
                        rets.append(True)
                    else:
                        rets.append(False)
            if term[1] == "!":
                ret = reduce(and_, rets)
            elif term[1] == ":":
                ret = reduce(or_, rets)
            else:
                print "Unable to parse colour string - invalid operator"
                pass
        elif term.startswith("o:"):
            if re.search(term[2:].replace('"', '').replace('~', card.get("name", "")), card.get("text", ""),  re.I):
                ret = True
        returnBools.append(ret)

    boolString = output % tuple(returnBools)
    res = boolExpr.parseString(boolString)[0]
    if bool(res) == True:
        return card

number_of_threads = 6

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=number_of_threads)
    multiprocessing.freeze_support

    colon_mode = oneOf("n o t in pow tou cmc r f a banned legal restricted is")
    colon_or_bang_mode = "c"
    math_mode = oneOf("mana pow tou cmc")
    colon_operator = ":"
    bang_operator = "!"
    math_operator = oneOf("= >= > <= < !")
    boolean_operators = oneOf("and not or")
    brackets = oneOf("( )")
    operand = (Word(alphanums) | dblQuotedString | Combine(Literal("{") + Word(alphanums+"\\") + Literal("}")))

    colon_total = colon_mode + colon_operator
    colon_or_bang_total = colon_or_bang_mode + oneOf([colon_operator, bang_operator])
    math_total = math_mode + math_operator

    total_thing = Combine( (colon_total | colon_or_bang_total | math_total) + operand )
    super_total = OneOrMore(Optional(brackets) + total_thing + Optional(brackets) + Optional(OneOrMore(boolean_operators)))

    ctrlc = 0

    def signal_handler(signal, frame):
        global ctrlc
        if ctrlc == 1:
            pool.close()
            pool.join()
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

    def printCard(card, extend=0, prepend="", quick=True):
        if quick:
            try:
                print prepend + card.get("name", "") + " (" + card.get("manaCost", "") + ")"
            except AttributeError:
                print prepend + card
        else:
            print card.get("name", "")
            if(card.get("names", None)):
                print "(Half of " + " // ".join(card.get("names")) + ")"
            if(card.get("manaCost")):
                print card.get("manaCost", "")
            else:
                print ", ".join(card.get("colors", []))
            print card.get("rarity", "")
            print " ".join(card.get("supertypes", [])) + (" " if card.get("supertypes", []) else "") + " ".join(card.get("types", [])) + (" - " if card.get("subtypes", []) else "") + " ".join(card.get("subtypes", []))
            if "Creature" in card.get("types", []):
                print card.get("power", "") + "/" + card.get("toughness", "")
            if "Planeswalker" in card.get("types", []):
                print "[" + str(card.get("loyalty", "")) + "]"
            print card.get("text", "").encode('utf-8') + "\n"
        if extend:
            print "\n\n----------\n"
            if type(card.get("printings")) is list:
                for p in card.get("printings", []):
                    print p
            else:
                print card.get("printings", "")
            print "----------\n"
            if extend > 0:
                if card.get("originalText", "") != card.get("text", ""):
                    print "-----------\n"
                    print card.get("originalText", "")
                    print card.get("originalType", "")
                    print "-----------\n"
                if card.get("rulings", []) != []:
                    for rule in card.get("rulings", []):
                        print rule["text"] + "\n"
                    print "----------\n"
                if card.get("legalities", {}) != {}:
                    for (k,va) in card.get("legalities", {}).items():
                        print k + " : " + va
            if extend > 1:
                print "\n" + card.get("flavor", "")
                print "Artist: " + card.get("artist", "") + "\n"

                for fPrint in card.get("foreignNames", []):
                    print fPrint["language"].encode("utf-8") + " : " + fPrint["name"].encode("utf-8")
            print "\n"

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

    # Load in all the cards
    try:
        with open('AllSets-x.json') as data_file:
            gatherer = json.load(data_file)
    except IOError:
        print "Unable to import cards - goodbye"
        sys.exit(0)

    # Loads in a list of the cards in the holiday cube
    try:
        with open('holidaycube.txt') as cube_file:
            cube_cards = cube_file.readlines()
    except IOError:
        print "Unable to import Holiday Cube list"
        cube_cards = []

    # Let's make an array with the list of all the card names, to help tab completion
    allCardNames = []
    for setname in gatherer.keys():
        allCardNames.extend([card["name"] for card in gatherer[setname]["cards"]])
    allCardNames = dedupe(allCardNames)
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
        o:FlyingDismember
    {1}{B/P}{B/P}

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
    #     mana<GGGGGG (Spells that can be cast with strictly less than six green mana)
    #     mana>=2RR mana<=6RR (Spells that cost two red mana and between two and six colorless mana)
    #     (new) mana>={2/R}
    #     (new) mana>={W/U}
    #     (new) mana>={U/P}
    #     mana!{G}{G} (Spells whose mana cost contains {G}{G})
    #     mana!P (Spells whose mana cost contains Phyrexian mana)
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
        print "\t<card name>* - search card names (allows for regexps)"
        print "\tdump <card name> - print raw JSON dump of the card (all printings)"
        print "\tt <text> - search rules text of cards (allows for regexps)"
        print "\tr <text> - search the comprehensive rules for text (allows for regexps)"
        print "\ts <text> - advanced search for cards with particular characteristics.  Type helpsearch for info"
        print "\trandom - gives a random card"
        print "\tprintsets - gives a list of all the sets I know about"
        print "\tprintsetsinorder - gives a list of all the sets in release date order"
        print "\tallcards <set> - gives a list of all the cards with a given set code (use printsets to get the code)"
        print "\tallcardsextend <set> - gives the text of all the cards with a given set code (use printsets to get the code)"
        print "\tbooster <set> - gives a randomly generated booster from either set code, or set name"
        print "\t\tbooster holidaycube <number> - gives an amount of randomly generated boosters from the MTGO Holiday Cube"
        print "\thelp - prints this help"
        print "\texit - goodbye :("

    # Print the help information initially
    help()

    while(1):
        card_name = raw_input(">: ")
        ctrlc = 0
        if(card_name == "" or card_name == "\n"):
            continue
        v = {}
        y = []

        # Display extended information about a card
        extend = False
        # Search card text instead of name
        text = False
        # Do a regular expression search of the card name
        match = False
        # Search terms instead of name
        search = False
        # Do a full JSON dump instead of pretty-print
        dump = False

        if card_name.startswith("t "):
            text = True
            card_name = card_name[2:]
        elif card_name.endswith("extend"):
            extend = True
            card_name = card_name[:-6]
        elif card_name.endswith("*"):
            match = True
            card_name = card_name[:-1]
        elif card_name.startswith("s "):
            search = True
            card_name = card_name[2:].lower()
            to_process = []
            output = ""
            try:
                parsed_data = super_total.parseString(card_name)
            except ParseException:
                print "Unable to parse search terms"
                continue

            last_was_s = False
            for idx, x in enumerate(parsed_data.asList()):
                if x in ["and", "or", "not"]:
                    output += " " + x + " "
                    last_was_s = False
                elif x == "(":
                    if last_was_s:
                      output += " and "
                    output += "("
                elif x == ")":
                    output += ")"
                else:
                    if last_was_s:
                        output += " and "
                    output += "%s"
                    to_process.append(x)
                    last_was_s = True

            cards = []
            partial_filter = partial(filter_function, terms=to_process, output=output)
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
            for setname in sorted(gatherer.keys()):
                print gatherer[setname].get("name", "") + " (" + setname + ")"
            pass
        elif card_name == "printsetsinorder":
            for setname in sorted(gatherer.keys(), key=lambda x: gatherer[x]['releaseDate']):
                print gatherer[setname].get("name", "") + " (" + setname + ")"
            pass
        elif card_name.startswith("allcards"):
            # Print out all the cards in a given set
            set_name = card_name.split(" ")[1]
            try:
                # TODO: Case insensitivity for set names
                cardlist = dedupe([x for x in gatherer[set_name]["cards"]], lambda x: x.get("name", ""))
                for card in cardlist:
                    printCard(card, quick=(0 if card_name.startswith("allcardsextend") else 1), extend=(1 if card_name.startswith("allcardsextend") else 0))
                print "\n" + str(len(cardlist)) + " result/s"
            except KeyError:
                print "Set not found"
            pass
        elif card_name.startswith("booster"):
            set_name = card_name[8:]
            booster = None
            already_picked = []
            if set_name.upper() in gatherer:
                # They've kindly given us the three letter set code
                booster = gatherer[set_name.upper()].get("booster", [])
            elif set_name.lower().startswith("holidaycube"):
                if cube_cards == []:
                    print "Holiday Cube not loaded"
                    continue
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
                        for setname in gatherer.keys():
                            y = [x for x in gatherer[setname]["cards"] if (x["name"] == card.rstrip() or x["name"].lower() == card.lower().rstrip())]
                            if y != []:
                                printCard(y[0])
                                break
                    print "-------\n"
                pass
            # They've probably given us the english name, let's try and find it
            else:
                for setname in gatherer.keys():
                    if gatherer[setname].get("name", "").lower() == set_name.lower():
                        booster = gatherer[setname].get("booster", [])
                        set_name = setname.lower()
            if booster != None and booster != []:
                if set_name != "vma" and set_name != "mma":
                    # 25% chance of having a foil
                    isFoil = (random.randint(1, 4) == 1)
                    if isFoil:
                        newbooster = booster[:]
                        # Replace a common with a foil
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
                        elif len(rarity) == 4 and set_name == "mma":
                            weighted_choices = [('foil mythic rare', 1), ('foil rare', 5), ('foil uncommon', 12), ('foil common', 18)]
                            population = [val for val, cnt in weighted_choices for i in range(cnt)]
                            rarity = random.choice(population)
                        elif len(rarity) == 2 and set_name == "isd":
                            rarity = "land"
                        else:
                            print "Weird list of rarities: "
                            print rarity
                            rarity = rarity[0]
                    try:
                        if set_name == "isd":
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"] if x["rarity"].lower() == rarity.lower() and x["layout"].lower() == "normal" and x["name"] not in already_picked])
                        else:
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"] if x["rarity"].lower() == rarity.lower() and "Conspiracy" not in x.get("types", []) and x["name"] not in already_picked])
                        printCard(card, prepend=rarity[0].upper() + ": ")
                        already_picked.append(card.get("name", ""))
                    except IndexError:
                        if rarity == "land":
                            print "L: " + random.choice(["Plains", "Island", "Swamp", "Mountain", "Forest"])
                        elif rarity == "foil" and set_name == "vma":
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"]  if x["name"] not in ["Black Lotus", "Timetwister", "Ancestral Recall", "Mox Ruby", "Mox Jet", "Mox Emerald", "Mox Sapphire", "Mox Pearl", "Time Walk"]])
                            printCard(card, prepend="Foil ")
                        elif rarity == "foil":
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"]] + ["Plains", "Island", "Swamp", "Mountain", "Forest"])
                            printCard(card, prepend="Foil ")
                        elif rarity == "draft-matters":
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"] if "Conspiracy" in x.get("types", [])])
                            print "Conspiracy (" + card.get("rarity", "")[0].upper() + "): " + card.get("name", "")
                        elif rarity == "marketing":
                            pass
                        elif rarity == "power nine":
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"] if x.get("name", "") in ["Black Lotus", "Timetwister", "Ancestral Recall", "Mox Ruby", "Mox Jet", "Mox Emerald", "Mox Sapphire", "Mox Pearl", "Time Walk"]])
                            # One in 28 chance of power 9 turning into foil power 9!
                            weighted_choices = [('', 27), ('Foil ', 1)]
                            population = [val for val, cnt in weighted_choices for i in range(cnt)]
                            extra = random.choice(population)
                            print extra + "Power 9! : " + card.get("name", "") + " (" + card.get("manaCost", "") + ")"
                        elif rarity.startswith("foil") and set_name == "mma":
                            card = random.choice([x for x in gatherer[set_name.upper()]["cards"] if x["rarity"].lower() == rarity[5:]])
                            printCard(card, prepend="Foil ")
                        elif rarity == "double faced":
                             card = random.choice([x for x in gatherer[set_name.upper()]["cards"] if x["layout"].lower() == "double-faced" and x.get("cmc", 0) != 0])
                             printCard(card, prepend="D: ")
                        else:
                            # No idea what we've encountered
                            print "Rarity: " + rarity
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
            pool.close()
            pool.join()
            sys.exit(0)
        elif card_name.startswith("dump "):
            dump = True
            card_name = card_name[5:]

        for setname in gatherer.keys():
            try:
                if text:
                    y = [x for x in gatherer[setname]["cards"] if re.search(card_name, (x.get("text", "")),  re.I)]
                elif match:
                    #y = [x for x in gatherer[setname]["cards"] if difflib.SequenceMatcher(None, x["name"].lower().split(",")[0], card_name.lower()).ratio() > 0.8]
                    y = [x for x in gatherer[setname]["cards"] if re.search(card_name.lower(), (x.get("name", "").lower()),  re.I)]
                elif search:
                    results = pool.map(partial_filter, gatherer[setname]["cards"])
                    #results = map(partial_filter, gatherer[setname]["cards"])
                    filtered_results = [x for x in results if x is not None]
                    if filtered_results != []:
                        y.extend(filtered_results)
                elif dump:
                    yy = [x for x in gatherer[setname]["cards"] if (x["name"].replace(u"Æ", "Ae") == card_name.rstrip() or x["name"].replace(u"Æ", "Ae").lower() == card_name.lower().rstrip())]
                    if yy != []:
                        print yy
                else:
                    y = [x for x in gatherer[setname]["cards"] if (x["name"].replace(u"Æ", "Ae") == card_name.rstrip() or x["name"].replace(u"Æ", "Ae").lower() == card_name.lower().rstrip())]
            except sre_constants.error:
                continue
            if y != []:
                for card in y:
                    v[card["name"]] = card

        # Print out the card/s
        if(v != {}):
            for name in sorted(v.keys()):
                printCard(v[name], quick=False, extend=(2 if extend else 0))
                print "\n"
            print str(len(v)) + " result/s"
