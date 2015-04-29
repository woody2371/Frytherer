from pyparsing import *
import json
import sys
import re
import multiprocessing
import signal
from functools import partial

number_of_threads = 2

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

colon_mode = oneOf("n o t in pow tou cmc r f a banned is")
colon_or_bang_mode = "c"
math_mode = oneOf("mana pow tou cmc")
colon_operator = ":"
bang_operator = "!"
math_operator = oneOf("= >= > <= <")
boolean_operators = oneOf("and not or")
brackets = oneOf("( )")
operand = (Word(alphanums) | dblQuotedString | Combine(Literal("{") + Word(alphanums) + Literal("}")))
 
colon_total = colon_mode + colon_operator
colon_or_bang_total = colon_or_bang_mode + oneOf([colon_operator, bang_operator])
math_total = math_mode + math_operator
 
total_thing = Combine( (colon_total | colon_or_bang_total | math_total) + operand )
super_total = OneOrMore(Optional(brackets) + total_thing + Optional(brackets) + Optional(boolean_operators))


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

# Load in all the cards
try:
    with open('AllSets-x.json') as data_file:
        print "Parsing all cards"
        gatherer = json.load(data_file)
except IOError:
    print "Unable to import cards - goodbye"
    sys.exit(0)

# Syntax Help

# All these options can be combined to more complicated queries: "a or b", "a not b", "a -b", "a (b or c)", "a or (b c)", and so on.

# Name:
#n:Birds of Paradise
#     n:!Anger (Match the full name)
# Rules Text (Oracle):
#o:Flying
#o:"First strike"
#o:{T} o:"add one mana of any color"
#o:"whenever ~ deals combat damage"
# Types (Oracle):
#t:angel
#t:"legendary angel"
#t:basic
#t:"arcane instant"
# Colors:
#     c:w (Any card that is white)
#     c:wu (Any card that is white or blue)
#     c:wum (Any card that is white or blue, and multicolored)
#     c!w (Cards that are only white)
#     c!wu (Cards that are only white or blue, or both)
#     c!wum (Cards that are only white and blue, and multicolored)
#     c!wubrgm (Cards that are all five colors)
#     c:m (Any multicolored card)
#     c:l or c:c (Lands and colorless cards)
# Color Identity:
#     ci:wu (Any card that is white or blue, but does not contain any black, red or green mana symbols)
# Color Indicator:
#     (new) in:wu (Any card that is white or blue according to the color indicator.)
# Mana Cost:
#     mana=3G (Spells that cost exactly 3G, or split cards that can be cast with 3G)
#     mana>=2WW (Spells that cost at least two white and two colorless mana)
#     mana<GGGGGG (Spells that can be cast with strictly less than six green mana)
#     mana>=2RR mana<=6RR (Spells that cost two red mana and between two and six colorless mana)
#     (new) mana>={2/R}
#     (new) mana>={W/U}
#     (new) mana>={UP}
# Power, Toughness, Converted Mana Cost:
#pow>=8
#tou<pow (All combinations are possible)
#cmc=7
#     (new) cmc>=*
# Rarity:
#     r:mythic
# Format:
#     f:standard (or block, extended, vintage, classic, legacy, modern, commander)
#     banned:extended (or legal, restricted)
# Artist:
#     a:"rk post"
# Is:
#     is:split, is:flip
#     is:vanilla (Creatures with no card text)
#     is:old, is:new, is:future (Old/new/future card face)
#     is:timeshifted
#     is:funny (Unglued/Unhinged/Happy Holidays Promos)
#     is:promo (Promotional cards)
#     is:promo is:old (Promotional cards with the original card face)
#     (new) is:permanent, is:spell
#     (new) is:black-bordered, is:white-bordered, is:silver-bordered

def filter_function(card, terms, output):
    returnBools = []
    values = {}

    values["pow"] = card.get("power", None)
    values["tou"] = card.get("toughness", None)
    values["cmc"] = card.get("cmc", None)
    types = " ".join(card.get("supertypes", [])) + (" " if card.get("supertypes", []) else "") + " ".join(card.get("types", [])) + " ".join(card.get("subtypes", []))

    for idx, term in enumerate(terms):
        ret = False
        if term.startswith("o:"):
            if re.search(term[2:].replace('"', '').replace('~', card.get("name", "")), card.get("text", ""),  re.I):
                ret = True
        elif term.startswith("n:"):
            if re.search(term[2:].replace('"', ''), card.get("name", ""), re.I):
                ret = True
        elif term.startswith("t:"):
            if re.search(term[2:].replace('"', '').replace(' ', '.*'), types, re.I):
                ret = True
        elif term.startswith("r:"):
            if re.search(term[2:].replace('"'), card.get("rarity", ""), re.I):
                ret = True
        elif term.startswith("c"):
            rets = []
            for y in term[2:]:
                if y == 'w' and 'White' in card.get("colors", []):
                    rets.append("True")
                else:
                    rets.append("False")
                if y == 'u' and 'Blue' in card.get("colors", []):
                    rets.append("True")
                else:
                    rets.append("False")
                if y == 'b' and 'Black' in card.get("colors", []):
                    rets.append("True")
                else:
                    rets.append("False")
                if y == 'r' and 'Red' in card.get("colors", []):
                    rets.append("True")
                else:   
                    rets.append("False")
                if y == 'g' and 'Green' in card.get("colors", []):
                    rets.append("True")
                else:
                    rets.append("False")
                if y == 'm' and len(card.get("colors", [])) > 1:
                    rets.append("True")
                else:
                    rets.append("False")
                if y == 'l' and 'Land' in card.get("types", []):
                    rets.append("True")
                else:
                    rets.append("False")
                if y == 'c' and len(card.get("colors", [])) > 0:
                    rets.append("True")
                else:
                    rets.append("False")
            if term[1] == "!":
                color_bool = " and ".join(rets)
            elif term[1] == ":":
                color_bool = " or ".join(rets)
            else:
                print "Unable to parse colour string - invalid operator"
                pass
            #print color_bool
            #print bool(boolExpr.parseString(color_bool)[0])
            ret = bool(boolExpr.parseString(color_bool)[0])
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
        returnBools.append(ret)

    boolString = output % tuple(returnBools)
    res = boolExpr.parseString(boolString)[0]
    if bool(res) == True:
        return card

def cardSearch(terms):
    print "Searching for " + terms

    term_space_split = terms.split(" ")
    to_process = []
    output = ""
    print "Parsing terms"
    parsed_data = super_total.parseString(terms)
    print parsed_data
    
    print "Generating output"
    last_was_s = False
    for idx, x in enumerate(parsed_data.asList()):
        print x
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

    print "To process:" + str(to_process)
    print "Output: " + output
    print output % tuple(to_process)

    cards = []
    partial_filter = partial(filter_function, terms=to_process, output=output)
    pool = multiprocessing.Pool(processes=number_of_threads)
    for setname in gatherer.keys():
    #for setname in ['ISD', 'DTK']:
        print "Searching " + setname
        results = pool.map(partial_filter, gatherer[setname]["cards"])
        #print "Searching done"
        filtered_results = [x for x in results if x is not None]
        if filtered_results != []:
            cards.append(filtered_results)

    pool.close()
    pool.join()

    return cards

if __name__ == "__main__":
    print "------- NUMBER OF SIMULTANEOUS THREADS -------"
    print str(number_of_threads)
    #terms = "pow>=8 and (cmc=7 or t:basic)"
    #terms = "pow>=8 and o:annihilator"
    #terms = "o:\"first strike\" and o:annihilator"
    #terms = "o:{T} o:\"add one mana of any color\""
    #terms = "o:\"whenever ~ deals combat damage\""
    #terms = "t:\"legendary angel\""
    #terms = "t:basic"
    terms = "c!wubrgm"
    print "Terms: " + terms
    x = cardSearch(terms)
    print "Done searching, now printing"
    for y in x:
        #print str(len(y))
        for card in y:
            print card.get("name")