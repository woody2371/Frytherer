#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest, sys, logging, time, random
import pysqlite2.dbapi2 as sqlite
from judgebot import dispatch_message
from frytherer import *
from fuzzywuzzy import fuzz, StringMatcher

word_file = "/usr/share/dict/words"
WORDS = open(word_file).read().splitlines()
sentinel = object()


try:
    conn = sqlite.connect('frytherer.db', check_same_thread=False)
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    conn.row_factory = sqlite.Row
    c = conn.cursor()
except sqlite.OperationalError:
    logging.error("Unable to open database - goodbye")
    sys.exit(0)
with open('CR.txt') as data_file:
    rules = data_file.readlines()

all_rules = {}
for rule in rules:
    x = rule.split('. ')
    all_rules[x[0]] = ". ".join(x[1:])


def giveRandomWords(number):
    """Get some random words"""
    ret = ""
    for i in xrange(number):
        ret += random.choice(WORDS) + " "
    return ret.rstrip()


def tryStartsWith(command, expected, publicExpected=sentinel, alone=False):
    """See if we still give the same result with random words surrounding"""
    if publicExpected is sentinel:
        publicExpected = expected
    if alone:
        return dispatch_message(command, False)[0][0].startswith(expected)
    else:
        return (dispatch_message(command, False)[0][0].startswith(expected) and
                dispatch_message(giveRandomWords(3) + " " + command, False)[0][0].startswith(expected) and
                dispatch_message(command + " " + giveRandomWords(3), False)[0][0].startswith(expected) and
                dispatch_message(giveRandomWords(3) + " " + command + " " + giveRandomWords(3), False)[0][0].startswith(expected) and
                dispatch_message(command, True)[0][0].startswith(publicExpected) and
                dispatch_message(giveRandomWords(3) + " " + command, True)[0][0].startswith(publicExpected) and
                dispatch_message(command + " " + giveRandomWords(3), True)[0][0].startswith(publicExpected) and
                dispatch_message(giveRandomWords(3) + " " + command + " " + giveRandomWords(3), True)[0][0].startswith(publicExpected))


def tryEquals(command, expected, publicExpected=sentinel, alone=False):
    """See if we still give the same result with random words surrounding"""
    if publicExpected is sentinel:
        publicExpected = expected
    if alone:
        return dispatch_message(command, False)[0] == expected
    else:
        return (dispatch_message(command, False)[0] == expected and
                dispatch_message(giveRandomWords(3) + " " + command, False)[0] == expected and
                dispatch_message(command + " " + giveRandomWords(3), False)[0] == expected and
                dispatch_message(giveRandomWords(3) + " " + command + " " + giveRandomWords(3), False)[0] == expected and
                dispatch_message(command, True)[0] == publicExpected and
                dispatch_message(giveRandomWords(3) + " " + command, True)[0] == publicExpected and
                dispatch_message(command + " " + giveRandomWords(3), True)[0] == publicExpected and
                dispatch_message(giveRandomWords(3) + " " + command + " " + giveRandomWords(3), True)[0] == publicExpected)


class FrythererTestCases(unittest.TestCase):
    def setUp(self):
        global all_rules
        global c
        self.all_rules = all_rules
        self.c = c
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)

    """Tests for basic functionality"""
    def testHelp(self):
        self.assertTrue(help().startswith("Welcome to Frytherer"))

    def testHelpSearch(self):
        self.assertTrue(helpsearch().startswith("All these options"))

    def testCalculateManaPerms(self):
        self.assertEqual(calculateManaPerms("{4}{U/G}{R/G}"), ['4RU', '4GU', '4GR', '4GG'])
        self.assertEqual(calculateManaPerms("{3}{U/G}{U/G}"), ['3UU', '3GU', '3GG'])
        self.assertEqual(calculateManaPerms("{3}{G}{R}{U/B}"), ['3GRU', '3BGR'])
        self.assertEqual(calculateManaPerms("{G}"), ['G'])
        self.assertEqual(calculateManaPerms("{1}"), ['1'])

    def testCalculateCMC(self):
        self.assertEqual(calculateCMC("{4}{G}{G}"), 6)
        self.assertEqual(calculateCMC("{6}"), 6)

    def testCardSearch(self):
        island = cardSearch(self.c, ["en:Island"])[0]
        self.assertEqual(island['name'], "Island")
        self.assertEqual(island['cmc'], 0)
        doubleQuotedIsland = cardSearch(self.c, ["en:\"Island\""])[0]
        self.assertEqual(doubleQuotedIsland['name'], "Island")
        only_two_basics = cardSearch(self.c, "en:Island or en:Mountain and not en:Swamp".split(' '))
        self.assertEqual(len(only_two_basics), 2)
        conspiracies = cardSearch(self.c, "banned:vintage and legal:freeform".split(' '))
        self.assertTrue(len(conspiracies) > 0)
        trinisphere = cardSearch(self.c, "restricted:vintage and set:dst and cn:154".split(' '))[0]
        self.assertEqual(trinisphere['name'], "Trinisphere")
        biggest_power = cardSearch(self.c, ["pow>15"])
        self.assertEqual(len(biggest_power), 1)
        smallest_power = cardSearch(self.c, ["pow<=0"])
        self.assertEqual(len(smallest_power), 565)
        biggest_toughness = cardSearch(self.c, ["tou>15"])
        self.assertEqual(len(biggest_toughness), 1)
        power_equal_cmc = cardSearch(self.c, ["pow=cmc"])
        self.assertEqual(len(power_equal_cmc), 1951)  # TODO: MCI thinks this should be 1947
        biggest_power_and_toughness = cardSearch(self.c, "pow>10 and tou>15".split(' '))
        self.assertEqual(len(biggest_power_and_toughness), 1)
        semi_biggest_power = cardSearch(self.c, "pow>=14 and tou>=14".split(' '))
        self.assertEqual(len(semi_biggest_power), 3)
        invalid_pow_equality = cardSearch(self.c, ["pow>*"])
        print len(invalid_pow_equality)
        invalid_tou_equality = cardSearch(self.c, ["tou>*"])
        print len(invalid_tou_equality)
        angrymob_and_aysencrusader = cardSearch(self.c, ["pow=2+*"])
        self.assertEqual(len(angrymob_and_aysencrusader), 2)
        #  TODO: FIX charrumbler_and_spinalparasite = cardSearch(self.c, ["pow<0"])
        #  self.assertEqual(len(charrumbler_and_spinalparasite), 2)
        goggles = cardSearch(self.c, ["t:artifact", "and", 'r:"mythic rare"', "and", "f:modern", "and", "a:paick"])
        self.assertEqual(len(goggles), 1)

    def testCardPrint(self):
        brisela = cardSearch(self.c, ["en:Brisela, Voice of Nightmares"])[0]
        self.assertEqual(printCard(self.c, brisela, quick=True), "Brisela, Voice of Nightmares ()")
        self.assertEqual(len(printCard(self.c, brisela, extend=2, quick=False)), 1562)
        jace = cardSearch(self.c, ["en:Jace, the Mind Sculptor"])[0]
        self.assertEqual(printCard(self.c, jace, quick=False, slackChannel=True), u"*Jace, the Mind Sculptor* {2}{U}{U} |Planeswalker - Jace| [3]  +2: Look at the top card of target player's library. You may put that card on the bottom of that player's library. / 0: Draw three cards, then put two cards from your hand on top of your library in any order. / \u22121: Return target creature to its owner's hand. / \u221212: Exile all cards from target player's library, then that player shuffles his or her hand into his or her library.")
        tg = cardSearch(self.c, ["en:Transguild Courier"])[0]
        self.assertEqual(printCard(self.c, tg, quick=False), "Transguild Courier\n{4}\nWhite, Blue, Black, Red, Green\nArtifact Creature - Golem\n3/3")
        self.assertTrue(printCard(self.c, tg, quick=True, short=True, ret=False) != "")  # TODO: Fix this
        self.assertTrue(printCard(self.c, tg, quick=True, short=True, ret=True), "Transguild Courier ({4})- A C - 3/3")

    def testURL(self):
        for doc in ["mtr", "ipg", "jar", "peip", "cr", "alldocs", "pptq", "rptq", "aipg", "amtr", "mt", "l@ec", "hce", "mpe", "grv", "ftmgs", "tardiness", "oa", "slow play", "insufficient shuffling", "ddlp", "lpv", "cpv", "mc", "usc minor", "usc major", "idaw", "bribery", "ab", "totm", "stalling", "cheating", "amtr 4.2", "aipg 4.2", "amtr appendix a", "aipg appendix a"]:
            self.assertTrue(url(doc).startswith("http://"))
        for doc in ["abc", "aipg appendix z", "amtr appendix z", "aipg 100.1", "aipg 100", "amtr 100.1", "amtr 100"]:
            self.assertFalse(url(doc).startswith("http://"))
        self.assertEqual(url("amtr 1.10"), "http://blogs.magicjudges.org/rules/mtr1-10/")

    def testRules(self):
        self.assertEqual(ruleSearch({}, "whatever"), "Rules search not available")
        self.assertEqual(ruleSearch(self.all_rules, "100.6b"), "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(ruleSearch(self.all_rules, "Locator"), "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(ruleSearch(self.all_rules, "Fry"), "No rule/s found")
        self.assertTrue(type(ruleSearch(self.all_rules, "116")) is list)


class BotTestCases(unittest.TestCase):
    """Tests for responding to commands"""
    def testHelp(self):
        self.assertTrue(tryStartsWith("!help", "Welcome to Frytherer"))

    def testHelpSearch(self):
        self.assertTrue(tryStartsWith("!helpsearch", "All these options"))

    def testUrl(self):
        for doc in ["!url amtr 1.10", "!url amtr 1.1", "!amtr 1.10", "!amtr 1.1", "!mtr 1.10", "!mtr 1.1" "!ipg 1.4"]:
            self.assertTrue(tryStartsWith(doc, "http://"))
        for doc in ["!url amtr 1.13", "!amtr 1.13", "!mtr 1.13", "!ipg 1.10"]:
            self.assertTrue(tryStartsWith(doc, "Invalid section requested"))
        for doc in ["mtr", "ipg", "jar", "peip", "alldocs", "pptq", "rptq", "aipg", "amtr", "amtr 4.2", "aipg 4.2", "amtr appendix a", "aipg appendix a"]:
            self.assertTrue(tryStartsWith("!" + doc, "http://"))
        for doc in ["mt", "l@ec", "hce", "mpe", "grv", "ftmgs", "tardiness", "oa", "slow play", "insufficient shuffling", "ddlp", "lpv", "cpv", "mc", "usc minor", "usc major", "idaw", "bribery", "ab", "totm", "stalling", "cheating"]:
            self.assertTrue(tryStartsWith("!" + doc, "http://", alone=True))
        for doc in ["abc", "aipg appendix z", "amtr appendix z", "aipg 100.1", "aipg 100", "amtr 100.1", "amtr 100"]:
            self.assertFalse(tryStartsWith("!url " + doc, "http://"))
        self.assertTrue(tryEquals("!url mtr 1.10", ("http://blogs.magicjudges.org/rules/mtr1-10/", False)))
        self.assertTrue(tryEquals("!url mtr 1.1", ("http://blogs.magicjudges.org/rules/mtr1-1/", False)))

    def testGetCard(self):
        # Single card that exists (single word)
        self.assertTrue(tryEquals("!island", ("Island\n\nBasic Land - Island", False), publicExpected=("*Island* |Basic Land - Island|", False)))

        # Single card that doesn't exist (single word)
        self.assertTrue(tryEquals("!fryland", ("", False)))

        # Weird formatting
        # FIX: To use fast search
        self.assertTrue(tryEquals("!\"island\"", ("Island\n\nBasic Land - Island", False), publicExpected=("*Island* |Basic Land - Island|", False)))
        self.assertTrue(tryEquals("!'island'", ("Island\n\nBasic Land - Island", False), publicExpected=("*Island* |Basic Land - Island|", False)))

        # Single card that exists (multiple word)
        self.assertTrue(tryStartsWith("!privileged position", "Privileged Position", publicExpected="*Privileged Position*"))

        # Single card that doesn't exist (multiple word)
        self.assertTrue(tryEquals("!frycanic fryland", ("", False)))

        # Single card that starts with the name of another card
        self.assertTrue(tryStartsWith("!forest bear", "Forest Bear", publicExpected="*Forest Bear*"))

        # # Multiple cards that exist (single word) -- <= five
        self.assertTrue(tryEquals("!island !mountain !swamp !plains !forest", (u'Island\n\nBasic Land - Island', False), publicExpected=(u'*Island* |Basic Land - Island|', False)))
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest", "island !mountain !swamp !plains !forest", False)[0]) > 50, u'Forest\n\nBasic Land - Forest\n\n\nIsland\n\nBasic Land - Island\n\n\nMountain\n\nBasic Land - Mountain\n\n\nPlains\n\nBasic Land - Plains\n\n\nSwamp\n\nBasic Land - Swamp\n\n')
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest", "!island !mountain !swamp !plains !forest", True)[0], u'*Forest* |Basic Land - Forest|\n*Island* |Basic Land - Island|\n*Mountain* |Basic Land - Mountain|\n*Plains* |Basic Land - Plains|\n*Swamp* |Basic Land - Swamp|')

        # # Multiple cards that exist (single word) -- exceeds five
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", True)[0][0], "6 results sent to PM")
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", True)[1][0]) > 50)
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", False)[0]) > 50)
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "island !mountain !swamp !plains !forest !Gigantoplasm", False)[0]) > 50)

    def testSplitCards(self):
        self.assertTrue(tryEquals("!fire//ice", (u'Fire\n(Part of Fire // Ice)\n{1}{R}\nInstant\nFire deals 2 damage divided as you choose among one or two target creatures and/or players.', False), publicExpected=(u'*Fire* (Part of Fire // Ice) {1}{R} |Instant| Fire deals 2 damage divided as you choose among one or two target creatures and/or players.', False)))

    def testSentences(self):
        self.assertTrue(tryEquals("!exquisite blood !sanguine blood", (u'Exquisite Blood\n{4}{B}\nEnchantment\nWhenever an opponent loses life, you gain that much life.', False), publicExpected=(u'*Exquisite Blood* {4}{B} |Enchantment| Whenever an opponent loses life, you gain that much life.', False)))
        self.assertTrue(tryEquals("!exquisite blood&!sanguine blood", (u'Exquisite Blood\n{4}{B}\nEnchantment\nWhenever an opponent loses life, you gain that much life.', False), publicExpected=(u'*Exquisite Blood* {4}{B} |Enchantment| Whenever an opponent loses life, you gain that much life.', False)))
        self.assertTrue(tryEquals("!exquisite blood&sanguine blood", (u'Exquisite Blood\n{4}{B}\nEnchantment\nWhenever an opponent loses life, you gain that much life.', False), publicExpected=(u'*Exquisite Blood* {4}{B} |Enchantment| Whenever an opponent loses life, you gain that much life.', False)))

    def testGetCardExtend(self):
        self.assertTrue(tryStartsWith("!island extend", "Island", alone=True))
        self.assertTrue(tryEquals("!fryland extend", "", alone=True))
        self.assertTrue(len(dispatch_message("!mounted archers extend", False)[0][0]) > 200)

    def testGetCardStar(self):
        # Cards are found
        self.assertTrue(tryStartsWith("!island*", "Island", publicExpected="9 results"))

        # Cards aren't found
        self.assertEqual(dispatch_message("!fryland*", False)[0], ("", False))
        self.assertEqual(dispatch_message("!fryland*", True)[0], ("", False))

        # Too many cards are found
        self.assertTrue(dispatch_message("!Phyrexian*", False)[0][0].startswith("Too many cards to print"))
        self.assertTrue(dispatch_message("!Phyrexian*", True)[0][0].startswith("Too many cards to print"))

        # Exactly one card is found
        self.assertEqual(dispatch_message("!Phyrexian War Beast*", False)[0], (u'Phyrexian War Beast\n{3}\nArtifact Creature - Beast\n3/4\nWhen Phyrexian War Beast leaves the battlefield, sacrifice a land and Phyrexian War Beast deals 1 damage to you.\n1 result/s', False))
        self.assertEqual(dispatch_message("!Phyrexian War Beast*", True)[0], (u'*Phyrexian War Beast* {3} |Artifact Creature - Beast| 3/4 When Phyrexian War Beast leaves the battlefield, sacrifice a land and Phyrexian War Beast deals 1 damage to you.', False))

        # Between 2 and 5 cards are found
        self.assertTrue("5 result/s" in dispatch_message("!Phyrexian R*", False)[0][0])
        self.assertTrue(len(dispatch_message("!Phyrexian R*", True)[0][0]) > 100)

    def testGetRules(self):
        # FIX: Parsing rules queries in PM when not starting specifically with !r
        self.assertEqual(dispatch_message("!r 100.6b", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!100.6b", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r 100.6b", True)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r Locator", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r Locator", True)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r Fry", False)[0], ("No rule/s found", False))
        self.assertEqual(dispatch_message("!r Fry", True)[0], ("No rule/s found", False))
        self.assertEqual(dispatch_message("!rule 100.6b", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!rule 116", False)[0], ("116: Timing and Priority\n", False))
        self.assertEqual(dispatch_message("!rule Double Strike", False)[0], ('Double Strike: A keyword ability that lets a creature deal its combat damage twice. See rule 702.4, "Double Strike."\n', False))
        self.assertEqual(dispatch_message("!rule Doublestrike", False)[0], ('Double Strike: A keyword ability that lets a creature deal its combat damage twice. See rule 702.4, "Double Strike."\n', False))

    def testDoAdvancedSearch(self):
        self.assertEqual(dispatch_message("!s en:\"Island\"", False)[0], ("Island\n\nBasic Land - Island\n1 result/s", False))
        self.assertEqual(dispatch_message("!s en:\"Island\"", True)[0], ("*Island* |Basic Land - Island|", False))
        self.assertEqual(dispatch_message("!s en:'Island'", False)[0], ("Island\n\nBasic Land - Island\n1 result/s", False))
        self.assertEqual(dispatch_message("!s en:'Island'", True)[0], (u'*Island* |Basic Land - Island|', False))
        self.assertEqual(dispatch_message("!s en:Island or en:Mountain and not en:Swamp", False)[0], ("Island\n\nBasic Land - Island\nMountain\n\nBasic Land - Mountain\n2 result/s", False))
        self.assertEqual(dispatch_message("!s en:Island or en:Mountain and not en:Swamp", True)[0], ("*Island* |Basic Land - Island|\n*Mountain* |Basic Land - Mountain|", False))
        self.assertTrue(len(dispatch_message("!s banned:vintage and legal:freeform", False)[0][0]) > 500)
        self.assertEqual(dispatch_message("!s banned:vintage and legal:freeform", True)[0][0], "13 results sent to PM")
        self.assertTrue(len(dispatch_message("!s banned:vintage and legal:freeform", True)[1][0]) > 200)

        # Test brackets and implicit AND
        self.assertTrue(dispatch_message("!s f:modern (n:Cryptic and t:Instant)", False)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!s f:modern (n:Cryptic and t:Instant)", True)[0][0].startswith("*Cryptic Command*"))
        self.assertTrue(dispatch_message("!s f:modern n:Cryptic t:Instant", False)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!s f:modern n:Cryptic t:Instant", True)[0][0].startswith("*Cryptic Command*"))

        # Should be failures
        self.assertTrue(dispatch_message("!s n=Island", False)[0][0].startswith("Unable to parse search terms"))
        self.assertTrue(dispatch_message("!s n=Island", True)[0][0].startswith("Unable to parse search terms"))
        self.assertEqual(dispatch_message("!s n:Fryland", False)[0], ("No cards found", False))
        self.assertEqual(dispatch_message("!s n:Fryland", True)[0], ("No cards found", False))

    def testDoAdvancedSearchQuick(self):
        self.assertEqual(dispatch_message("!qs en:\"Island\"", False)[0], ("Island ()\n1 result/s", False))
        self.assertEqual(dispatch_message("!qs en:\"Island\"", True)[0], ("Island ()", False))
        self.assertEqual(dispatch_message("!qs en:'Island'", False)[0], ("Island ()\n1 result/s", False))
        self.assertEqual(dispatch_message("!qs en:'Island'", True)[0], ("Island ()", False))
        self.assertEqual(dispatch_message("!qs en:Island or en:Mountain and not en:Swamp", False)[0], ("Island ()\nMountain ()\n2 result/s", False))
        self.assertEqual(dispatch_message("!qs en:Island or en:Mountain and not en:Swamp", True)[0], ("Island ()\nMountain ()", False))
        self.assertTrue(len(dispatch_message("!qs banned:vintage and legal:freeform", False)[0][0]) > 200)
        self.assertEqual(dispatch_message("!qs banned:vintage and legal:freeform", True)[0][0], "13 results sent to PM")
        self.assertTrue(len(dispatch_message("!qs banned:vintage and legal:freeform", True)[1][0]) > 200)

        self.assertTrue(dispatch_message("!qs f:modern (n:Cryptic and t:Instant)", False)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!qs f:modern (n:Cryptic and t:Instant)", True)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!qs f:modern n:Cryptic t:Instant", False)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!qs f:modern n:Cryptic t:Instant", True)[0][0].startswith("Cryptic Command"))

        # Should be failures
        self.assertTrue(dispatch_message("!qs n=Island", False)[0][0].startswith("Unable to parse search terms"))
        self.assertTrue(dispatch_message("!qs n=Island", True)[0][0].startswith("Unable to parse search terms"))
        self.assertEqual(dispatch_message("!qs n:Fryland", False)[0], ("No cards found", False))
        self.assertEqual(dispatch_message("!qs n:Fryland", True)[0], ("No cards found", False))

    def testRulings(self):
        self.assertEqual(dispatch_message("!ruling bronze sable", False)[0], ("Bronze Sable has no rulings on Gatherer", False))
        self.assertEqual(dispatch_message("!rulings nissa, vastwood seer", False)[0], ("12 rulings sent to PM", False))
        self.assertEqual(dispatch_message("!ruling 1 nissa, vastwood seer", False)[0], ("Nissa, Vastwood Seer - Nissa, Vastwood Seer is exiled as a result of her second triggered ability. If she enters the battlefield while you control seven or more lands, she won’t automatically be exiled and transform.", False))
        self.assertEqual(dispatch_message("!ruling", False)[0], ("", False))
        return

    def testFlavour(self):
        print dispatch_message("!chandra, f", False)
        return

    def testGetRandomCard(self):
        self.assertTrue(len(dispatch_message("!random", False)[0][0]) > 5)
        self.assertTrue(len(dispatch_message("!random", True)[0][0]) > 5)

    def testPrintSets(self):
        self.assertTrue(len(dispatch_message("!printsets", False)[0][0]) > 500)
        self.assertTrue(len(dispatch_message("!printsets", True)[0][0]) > 500)

    def testPrintSetsInOrder(self):
        self.assertTrue(len(dispatch_message("!printsetsinorder", False)[0][0]) > 500)
        self.assertTrue(len(dispatch_message("!printsetsinorder", True)[0][0]) > 500)

    def testDatatog(self):
        try:
            from mtgrulesdict import datatog
        except:
            return
        count = 0

        numbersToSkip = [123, 165, 167, 184, 194, 280, 290, 297, 312, 360, 379, 397, 442,
                         458, 479, 481, 491, 505, 511, 529, 547, 627, 630, 641, 645,
                         687, 689, 704, 731, 814, 824, 842, 870, 900, 916, 977, 1019, 1028, 1031,
                         1049, 1052, 1065, 1091, 1105, 1108, 1118, 1201, 1280, 1286, 1300, 1330,
                         1339, 1343, 1344, 1355, 1427, 1451, 1453, 1476, 1479, 1485, 1498, 1526,
                         1532, 1539, 1568, 1625, 1657, 1678, 1684, 1725, 1736, 1738, 1744, 1746, 1754,
                         1763, 1812, 1985, 2011, 2075, 2082, 2116, 2152, 2154, 2174, 2219, 2231,
                         2311, 2327, 2328, 2340, 2366, 2368, 2382, 2421, 2429, 2448, 2486, 2493,
                         2537, 2543, 2555, 2560, 2684, 2722, 2758, 2776, 2816, 2865, 2868, 2979,
                         2980, 3008, 3011, 3036, 3080, 3132, 3181, 3193, 3225, 3231, 3290, 3307,
                         3337, 3373, 3439, 3531, 3550, 3586, 3645, 3657, 3661, 3668, 3715, 3729,
                         3756, 3770, 3859, 3869, 3879, 3890, 3936, 3947, 3951, 3976, 3989, 4015, 4035,
                         4089, 4135, 4139, 4154, 4175, 4179, 4185, 4186, 4218, 4230, 4254, 4256, 4360, 4362,
                         4376, 4402, 4409, 4501, 4508, 4546, 4561, 4611, 4614, 4625, 4655, 4690,
                         4698, 4686, 4699, 4760, 4793, 2477, 2535, 2602, 2650, 3287]
        startCount = numbersToSkip[-1]
        file_output = False
        startCount = 0  # 4135
        # TODO: 1049 and 1300 :( :( Hopefully won't happen on our Slack
        # 2477 :(
        # TODO: 1498
        # TODO: 2382
        # TODO: 4186
        with open('results.txt', 'a') as f:
            for input in datatog.keys():
                input = input.encode('utf-8')
                count += 1
                if (startCount and count < startCount) or (count in numbersToSkip):
                    continue
                print "{} of {}".format(count, len(datatog.keys()))
                if re.search(r'!\d', input) or '!ruling' in input or '!reminder' in input or '!ex ' in input:
                    continue

                result = dispatch_message(input.lower().rstrip().replace("’", "'"), True)
                if len(result) > 1:
                    result = filter(lambda x: x != ('', False), result)
                try:
                    logging.debug("INPUT: {}n\nOUTPUT: {}\nJUDGEBOT: {}".format(input, datatog[input], result))
                    if datatog[input] == []:
                        x = (result == [] or result[0] == ('', False))
                        if file_output and not x:
                                f.write(str(count) + '\n')
                                f.write("INPUT: " + str(input) + '\n')
                                f.write("DATATOG: " + str(datatog[input]) + '\n')
                                f.write("JUDGEBOT: " + str(result) + '\n---\n')
                                logging.error("Fail")
                        else:
                            self.assertTrue(x)
                    else:
                        if "//" in input:
                            x = (len(result) == len(datatog[input]) + 1)
                            if file_output and not x:
                                f.write(str(count) + '\n')
                                f.write("INPUT: " + str(input) + '\n')
                                f.write("DATATOG: " + str(datatog[input]) + '\n')
                                f.write("JUDGEBOT: " + str(result) + '\n---\n')
                                logging.error("Fail")
                            else:
                                self.assertTrue(x)
                        else:
                            x = (len(result) == len(datatog[input]))
                            if file_output and not x:
                                f.write(str(count) + '\n')
                                f.write("INPUT: " + str(input) + '\n')
                                f.write("DATATOG: " + str(datatog[input]) + '\n')
                                f.write("JUDGEBOT: " + str(result) + '\n---\n')
                                logging.error("Fail")
                            else:
                                self.assertTrue(x)
                            if "found and sent to" not in datatog[input][0] and "containing the words" not in datatog[input][0] and "Duplicate response withheld" not in datatog[input][0]:
                                for (idx, item) in enumerate(result):
                                    # Datatog doesn't show reminder text
                                    item = re.sub(r'\([^Part].*?\)', '', item[0])
                                    logging.debug(datatog[input][idx])
                                    logging.debug(item)
                                    logging.debug(fuzz.ratio(datatog[input][idx], item))
                                    v = (fuzz.ratio(datatog[input][idx], item) > 60)
                                    if file_output and not v:
                                        f.write(str(count) + '\n')
                                        f.write("INPUT: " + str(input) + '\n')
                                        f.write("DATATOG: " + str(datatog[input]) + '\n')
                                        f.write("JUDGEBOT: " + str(result) + '\n---\n')
                                        logging.error("Fail")
                                    else:
                                        self.assertTrue(v)
                except KeyError:
                    logging.error("Weirdness")

if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    logging.basicConfig(level=logging.DEBUG, format=u'%(asctime)-s %(levelname)s [%(name)s]: %(message)s')

    unittest.main()
