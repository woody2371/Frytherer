#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import unittest, sys, logging
import pysqlite2.dbapi2 as sqlite
from judgebot import dispatch_message
from frytherer import *


class FrythererTestCases(unittest.TestCase):
    def setUp(self):
        reload(sys)  # Reload does the trick!
        sys.setdefaultencoding('UTF8')
        logging.basicConfig(level=logging.DEBUG)
        try:
            conn = sqlite.connect('frytherer.db', check_same_thread=False)
            conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
            conn.row_factory = sqlite.Row
            self.c = conn.cursor()
        except sqlite.OperationalError:
            logging.error("Unable to open database - goodbye")
            sys.exit(0)
        with open('CR.txt') as data_file:
            rules = data_file.readlines()

        self.all_rules = {}
        for rule in rules:
            x = rule.split('. ')
            self.all_rules[x[0]] = ". ".join(x[1:])

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
        only_two_basics = cardSearch(self.c, "en:Island or en:Mountain and not en:Swamp".split(' '))
        self.assertEqual(len(only_two_basics), 2)
        conspiracies = cardSearch(self.c, "banned:vintage and legal:freeform".split(' '))
        self.assertTrue(len(conspiracies) > 0)
        trinisphere = cardSearch(self.c, "restricted:vintage and set:dst and cn:154".split(' '))[0]
        self.assertEqual(trinisphere['name'], "Trinisphere")
        biggest_power = cardSearch(self.c, "pow>15 and tou>15".split(' '))
        self.assertEqual(len(biggest_power), 1)

    def testCardPrint(self):
        brisela = cardSearch(self.c, ["en:Brisela, Voice of Nightmares"])[0]
        self.assertEqual(printCard(self.c, brisela, quick=True), "Brisela, Voice of Nightmares ()")
        self.assertEqual(len(printCard(self.c, brisela, extend=2, quick=False)), 1563)
        jace = cardSearch(self.c, ["en:Jace, the Mind Sculptor"])[0]
        self.assertEqual(printCard(self.c, jace, quick=False, slackChannel=True), "*Jace, the Mind Sculptor* {2}{U}{U} |Planeswalker - Jace| [3]  +2: Look at the top card of target player's library. You may put that card on the bottom of that player's library. / 0: Draw three cards, then put two cards from your hand on top of your library in any order. / −1: Return target creature to its owner's hand. / −12: Exile all cards from target player's library, then that player shuffles his or her hand into his or her library.")
        tg = cardSearch(self.c, ["en:Transguild Courier"])[0]
        self.assertEqual(printCard(self.c, tg, quick=False), "Transguild Courier\n{4}\nWhite, Blue, Black, Red, Green\nArtifact Creature - Golem\n3/3\n\n")
        self.assertTrue(printCard(self.c, tg, quick=True, short=True, ret=False) != "")  # TODO: Fix this
        self.assertTrue(printCard(self.c, tg, quick=True, short=True, ret=True), "Transguild Courier ({4})- A C - 3/3")

    def testURL(self):
        for doc in ["mtr", "ipg", "jar", "peip", "cr", "alldocs", "pptq", "rptq", "aipg", "amtr", "mt", "l@ec", "hce", "mpe", "grv", "ftmgs", "tardiness", "oa", "slow play", "insufficient shuffling", "ddlp", "lpv", "cpv", "mc", "usc minor", "usc major", "idaw", "b&w", "ab", "totm", "stalling", "cheating", "amtr 4.2", "aipg 4.2", "amtr appendix a", "aipg appendix a"]:
            self.assertTrue(url(doc).startswith("http://"))
        for doc in ["abc", "aipg appendix z", "amtr appendix z", "aipg 100.1", "aipg 100", "amtr 100.1", "amtr 100"]:
            self.assertFalse(url(doc).startswith("http://"))

    def testRules(self):
        self.assertEqual(ruleSearch({}, "whatever"), "Rules search not available")
        self.assertEqual(ruleSearch(self.all_rules, "100.6b"), "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(ruleSearch(self.all_rules, "Locator"), "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(ruleSearch(self.all_rules, "Fry"), "No rule/s found")


class BotTestCases(unittest.TestCase):
    """Tests for responding to commands"""
    def testHelp(self):
        self.assertTrue(dispatch_message("help", "!help", False)[0].startswith("Welcome to Frytherer"))
        self.assertTrue(dispatch_message("help", "help", False)[0].startswith("Welcome to Frytherer"))
        self.assertTrue(dispatch_message("help", "!help", True)[0].startswith("Welcome to Frytherer"))

    def testHelpSearch(self):
        self.assertTrue(dispatch_message("helpsearch", "!helpsearch", False)[0].startswith("All these options"))
        self.assertTrue(dispatch_message("helpsearch", "helpsearch", False)[0].startswith("All these options"))
        self.assertTrue(dispatch_message("helpsearch", "!helpsearch", True)[0].startswith("All these options"))

    def testUrl(self):
        self.assertTrue(dispatch_message("url cr", "!url cr", False)[0].startswith("http://"))
        self.assertTrue(dispatch_message("url cr", "url cr", False)[0].startswith("http://"))
        self.assertTrue(dispatch_message("url cr", "!url cr", True)[0].startswith("http://"))

    def testGetCard(self):
        pass

    def testGetCardExtend(self):
        pass

    def testGetRulesFromR(self):
        pass

    def testGetRulesFromNumber(self):
        pass

    def testDoAdvancedSearch(self):
        pass

    def testDoAdvancedSearchQuick(self):
        pass

    def testGetRandomCard(self):
        self.assertTrue(len(dispatch_message("random", "!random", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("random", "random", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("random", "!random", True)[0]) > 5)

    def testPrintSets(self):
        pass

    def testPrintSetsInOrder(self):
        pass


if __name__ == '__main__':
    unittest.main()
