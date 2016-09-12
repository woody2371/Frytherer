#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest, sys, logging, time
import pysqlite2.dbapi2 as sqlite
from judgebot import dispatch_message, handle_private_message
from frytherer import *

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


def tryStartsWith(command, expected):
    return (dispatch_message(command, False)[0][0].startswith(expected) and
            dispatch_message("Some Words Before " + command, False)[0][0].startswith(expected) and
            dispatch_message(command + " Some Words After", False)[0][0].startswith(expected) and
            dispatch_message("Some Words Before " + command + " Some Words After", False)[0][0].startswith(expected) and
            dispatch_message(command, True)[0][0].startswith(expected) and
            dispatch_message("Some Words Before " + command, True)[0][0].startswith(expected) and
            dispatch_message(command + " Some Words After", True)[0][0].startswith(expected) and
            dispatch_message("Some Words Before " + command + " Some Words After", True)[0][0].startswith(expected))


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


class BotTestCases(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
        # Shit should be fast
        # self.assertTrue(t < 1)

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
        for doc in ["mtr", "ipg", "jar", "peip", "cr", "alldocs", "pptq", "rptq", "aipg", "amtr", "mt", "l@ec", "hce", "mpe", "grv", "ftmgs", "tardiness", "oa", "slow play", "insufficient shuffling", "ddlp", "lpv", "cpv", "mc", "usc minor", "usc major", "idaw", "bribery", "ab", "totm", "stalling", "cheating", "amtr 4.2", "aipg 4.2", "amtr appendix a", "aipg appendix a"]:
            self.assertTrue(tryStartsWith(doc, "http://"))
        for doc in ["abc", "aipg appendix z", "amtr appendix z", "aipg 100.1", "aipg 100", "amtr 100.1", "amtr 100"]:
            self.assertFalse(tryStartsWith("!url " + doc, "http://"))
        self.assertEqual(dispatch_message("!url mtr 1.10", False)[0], ("http://blogs.magicjudges.org/rules/mtr1-10/", False))
        self.assertEqual(dispatch_message("!url mtr 1.10", True)[0], ("http://blogs.magicjudges.org/rules/mtr1-10/", False))
        self.assertEqual(dispatch_message("!url mtr 1.1", False)[0], ("http://blogs.magicjudges.org/rules/mtr1-1/", False))
        self.assertEqual(dispatch_message("!url mtr 1.1", True)[0], ("http://blogs.magicjudges.org/rules/mtr1-1/", False))

    def testGetCard(self):
        # Single card that exists (single word)
        self.assertEqual(dispatch_message("!island", False)[0], ("Island\n\nBasic Land - Island", False))
        self.assertEqual(dispatch_message("!island", True)[0], ("*Island* |Basic Land - Island|", False))

        # Single card that doesn't exist (single word)
        self.assertEqual(dispatch_message("!fryland", False)[0], ("", False))
        self.assertEqual(dispatch_message("!fryland", True)[0], ("", False))

        # Weird formatting
        # FIX: To use fast search
        self.assertEqual(dispatch_message("!\"island\"", False)[0], ("Island\n\nBasic Land - Island", False))
        self.assertEqual(dispatch_message("!\"island\"", True)[0], ("*Island* |Basic Land - Island|", False))
        self.assertEqual(dispatch_message("!'island'", False)[0], ("Island\n\nBasic Land - Island", False))
        self.assertEqual(dispatch_message("!'island'", True)[0], ("*Island* |Basic Land - Island|", False))

        # Single card that exists (multiple word)
        self.assertTrue(dispatch_message("!privileged position", False)[0][0].startswith("Privileged Position"))
        self.assertTrue(dispatch_message("!privileged position", True)[0][0].startswith("*Privileged Position"))

        # Single card that doesn't exist (multiple word)
        self.assertEqual(dispatch_message("!frycanic fryland", False)[0], ("", False))
        self.assertEqual(dispatch_message("!frycanic fryland", True)[0], ("", False))

        # # Multiple cards that exist (single word) -- <= five
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest", "!island !mountain !swamp !plains !forest", False)[0], u'Forest\n\nBasic Land - Forest\nIsland\n\nBasic Land - Island\nMountain\n\nBasic Land - Mountain\nPlains\n\nBasic Land - Plains\nSwamp\n\nBasic Land - Swamp')
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest", "island !mountain !swamp !plains !forest", False)[0]) > 50, u'Forest\n\nBasic Land - Forest\n\n\nIsland\n\nBasic Land - Island\n\n\nMountain\n\nBasic Land - Mountain\n\n\nPlains\n\nBasic Land - Plains\n\n\nSwamp\n\nBasic Land - Swamp\n\n')
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest", "!island !mountain !swamp !plains !forest", True)[0], u'*Forest* |Basic Land - Forest|\n*Island* |Basic Land - Island|\n*Mountain* |Basic Land - Mountain|\n*Plains* |Basic Land - Plains|\n*Swamp* |Basic Land - Swamp|')

        # # Multiple cards that exist (single word) -- exceeds five
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", True)[0][0], "6 results sent to PM")
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", True)[1][0]) > 50)
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", False)[0]) > 50)
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "island !mountain !swamp !plains !forest !Gigantoplasm", False)[0]) > 50)

    def testSentences(self):
        pass

    def testGetCardExtend(self):
        self.assertTrue(len(dispatch_message("!island extend", False)[0][0]) > 50)
        self.assertTrue(len(dispatch_message("!island extend", True)[0][0]) > 50)
        self.assertEqual(dispatch_message("!fryland extend", False)[0], "")
        self.assertEqual(dispatch_message("!fryland extend", True)[0], "")

    def testGetCardStar(self):
        # Cards are found
        self.assertTrue(len(dispatch_message("!island*", False)[0][0]) > 50)
        self.assertEqual(dispatch_message("!island*", True)[0][0], "9 results sent to PM")
        self.assertTrue(len(dispatch_message("!island*", True)[1][0]) > 50)

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
        self.assertTrue(len(dispatch_message("!Phyrexian R*", True)[0][0]) > 50)

    def testGetRules(self):
        # FIX: Parsing rules queries in PM when not starting specifically with !r
        self.assertEqual(dispatch_message("!r 100.6b", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!100.6b", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r 100.6b", True)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r Locator", False)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r Locator", True)[0], ("100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n", False))
        self.assertEqual(dispatch_message("!r Fry", False)[0], ("No rule/s found", False))
        self.assertEqual(dispatch_message("!r Fry", True)[0], ("No rule/s found", False))

    def testDoAdvancedSearch(self):
        self.assertEqual(dispatch_message("!s en:\"Island\"", False)[0], ("Island\n\nBasic Land - Island\n1 result/s", False))
        self.assertEqual(dispatch_message("!s en:\"Island\"", True)[0], ("*Island* |Basic Land - Island|", False))
        self.assertEqual(dispatch_message("!s en:'Island'", False)[0], ("Island\n\nBasic Land - Island\n1 result/s", False))
        self.assertEqual(dispatch_message("!s en:'Island'", True)[0], (u'*Island* |Basic Land - Island|', False))
        self.assertEqual(dispatch_message("!s en:Island or en:Mountain and not en:Swamp", False)[0], ("Island\n\nBasic Land - Island\nMountain\n\nBasic Land - Mountain\n2 result/s", False))
        self.assertEqual(dispatch_message("!s en:Island or en:Mountain and not en:Swamp", True)[0], ("*Island* |Basic Land - Island|\n*Mountain* |Basic Land - Mountain|", False))
        self.assertTrue(len(dispatch_message("!s banned:vintage and legal:freeform", False)[0][0]) > 50)
        self.assertEqual(dispatch_message("!s banned:vintage and legal:freeform", True)[0][0], "13 results sent to PM")
        self.assertTrue(len(dispatch_message("!s banned:vintage and legal:freeform", True)[1][0]) > 50)

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
        self.assertTrue(len(dispatch_message("!qs banned:vintage and legal:freeform", False)[0][0]) > 50)
        self.assertEqual(dispatch_message("!qs banned:vintage and legal:freeform", True)[0][0], "13 results sent to PM")
        self.assertTrue(len(dispatch_message("!qs banned:vintage and legal:freeform", True)[1][0]) > 50)

        self.assertTrue(dispatch_message("!qs f:modern (n:Cryptic and t:Instant)", False)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!qs f:modern (n:Cryptic and t:Instant)", True)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!qs f:modern n:Cryptic t:Instant", False)[0][0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("!qs f:modern n:Cryptic t:Instant", True)[0][0].startswith("Cryptic Command"))

        # Should be failures
        self.assertTrue(dispatch_message("!qs n=Island", False)[0][0].startswith("Unable to parse search terms"))
        self.assertTrue(dispatch_message("!qs n=Island", True)[0][0].startswith("Unable to parse search terms"))
        self.assertEqual(dispatch_message("!qs n:Fryland", False)[0], ("No cards found", False))
        self.assertEqual(dispatch_message("!qs n:Fryland", True)[0], ("No cards found", False))

    def testGetRandomCard(self):
        self.assertTrue(len(dispatch_message("!random", False)[0][0]) > 5)
        self.assertTrue(len(dispatch_message("!random", True)[0][0]) > 5)

    def testPrintSets(self):
        self.assertTrue(len(dispatch_message("!printsets", False)[0][0]) > 5)
        self.assertTrue(len(dispatch_message("!printsets", True)[0][0]) > 5)

    def testPrintSetsInOrder(self):
        self.assertTrue(len(dispatch_message("!printsetsinorder", False)[0][0]) > 5)
        self.assertTrue(len(dispatch_message("!printsetsinorder", True)[0][0]) > 5)


if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    logging.basicConfig(level=logging.DEBUG)

    unittest.main()
