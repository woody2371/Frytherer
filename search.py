#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import json
#import difflib
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

ctrlc = 0

def signal_handler(signal, frame):
    global ctrlc
    if ctrlc == 1:
        sys.exit(0)
    else:
        sys.stdout.write("\nPress Ctrl-C again to exit\n>: ")
        sys.stdout.flush()
        ctrlc = 1

# Capture Ctrl-C (make them do it twice to exit)
signal.signal(signal.SIGINT, signal_handler)

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

def cardSearch(card):
    if terms.has_key('cost'):
        if (card.get("manaCost", "").lower() == terms['cost'].lower()) or (card.get("manaCost", "").encode('utf-8').lower().translate(None, "{}") == terms['cost'].lower()):
            cost = True
        else:
            cost = False
    else:
        cost = True
    if terms.has_key('type'):
        if terms['type'].lower() in [x.lower() for x in card.get("supertypes", []) + card.get("types", []) + card.get("subtypes", [])]:
            typ = True
        else:
            typ = False
    else:
        typ = True
    if terms.has_key('rarity'):
        if card.get("rarity", "").lower() == terms['rarity'].lower():
            rarity = True
        else:
            rarity = False
    else:
        rarity = True
    if terms.has_key('text'):
        if re.search(terms['text'], (card.get("text", "")),  re.I):
            text = True
        else:
            text = False
    else:
        text = True
    if terms.has_key('p'):
        if card.get("power", "") == terms['p']:
            power = True
        else:
            power = False
    else:
        power = True
    if terms.has_key('t'):
        if card.get("toughness", "") == terms['t']:
            toughness = True
        else:
            toughness = False
    else:
        toughness = False
    return (cost and typ and rarity and text and power and toughness)

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

def cardname_completer(text, state):
    options = [x for x in allCardNames if x.lower().startswith(text.lower())] + [None]
    if state < len(options):
        return options[state]
    else:
        return None

# Activate tab complete
if readline.__doc__ != None and 'libedit' in readline.__doc__:
    print "Mac Tab Mode Active, your tab complete is going to be a bit shit! :(\n"
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

readline.set_completer_delims('')
readline.set_completer(cardname_completer)

# Syntax Help

# All these options can be combined to more complicated queries: "a or b", "a not b", "a -b", "a (b or c)", "a or (b c)", and so on.

# Name:
#     Birds of Paradise
#     "Birds of Paradise"
#     !Anger (Match the full name)
# Rules Text (Oracle):
#     o:Flying
#     o:"First strike"
#     o:{T} o:"add one mana of any color"
#     (new) o:"whenever ~ deals combat damage"
# Types (Oracle):
#     t:angel
#     t:"legendary angel"
#     t:basic
#     t:"arcane instant"
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
#     pow>=8
#     tou<pow (All combinations are possible)
#     cmc=7
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
#     is:funny, not:funny (Unglued/Unhinged/Happy Holidays Promos)
#     is:promo (Promotional cards)
#     is:promo is:old (Promotional cards with the original card face)
#     (new) is:permanent, is:spell
#     (new) is:black-bordered, is:white-bordered, is:silver-bordered

def help():
    print "Welcome to Frytherer.  Your options are:"
    print "\t<card name> - gives what's on the card (allows for tab complete)"
    print "\t<card name> extend - gives extended info about the card (everything - rulings, legality, artist, flavour text, foreign names)"
    print "\t<card name>* - search card names (allows for regexps)"
    print "\tt <text> - search rules text of cards (allows for regexps)"
    print "\tr <text> - search the comprehensive rules for text (allows for regexps)"
    print "\ts <text> - search for cards with particular characteristics"
    print "\t\tcost=2UBR - search for costs"
    print "\t\ttype=creature - search for card/super/sub type"
    print "\t\trarity=common - search for card rarity"
    print "\t\ttext=trample - search for rules text"
    print "\t\tp=3 - search for power"
    print "\t\tt=4 - search for toughness"
    print "\trandom - gives a random card"
    print "\tprintsets - gives a list of all the sets I know about"
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

    # Display extended information about a card
    extend = False
    # Search card text instead of name
    text = False
    # Do a regular expression search of the card name
    match = False
    # Search terms instead of name
    search = False

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
        card_name = card_name[2:]
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
    elif card_name == "exit":
        sys.exit(0)

    for setname in gatherer.keys():
        try:
            if text:
                y = [x for x in gatherer[setname]["cards"] if re.search(card_name, (x.get("text", "")),  re.I)]
            elif match:
                #y = [x for x in gatherer[setname]["cards"] if difflib.SequenceMatcher(None, x["name"].lower().split(",")[0], card_name.lower()).ratio() > 0.8]
                y = [x for x in gatherer[setname]["cards"] if re.search(card_name.lower(), (x.get("name", "").lower()),  re.I)]
            elif search:
                terms = {}
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
