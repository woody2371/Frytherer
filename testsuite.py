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
    class Channel(object):
        # Mock slack channel
        def __init__(self):
            self._body = {}
            self._body['name'] = '#TestChan'

    class Client(object):
        # Mock slack client
        def __init__(self):
            self.channels = {}
            self.users = {}
            self.users['Fry'] = {}
            self.users['Fry']['real_name'] = "Fry Frybergenstein"

    class Message(object):
        # Mock message to pretend we're slack
        def __init__(self, client, channel):
            self._client = client
            self.channel = channel
            self.body = {}
            self.body['channel'] = "Test Channel"
            self.body['user'] = "Fry"

        def reply(self, test):
            print test

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print "%s: %.3f" % (self.id(), t)
        # Shit should be fast
        # self.assertTrue(t < 1)

    """Tests for responding to commands"""
    def testHelp(self):
        # cl = self.Client()
        # ch = self.Channel()
        # m = self.Message(cl, ch)
        # m.body['text'] = "help"
        # handle_private_message(m, m.body['text'])
        # m.body['text'] = "!help"
        # handle_private_message(m, m.body['text'])
        self.assertTrue(dispatch_message("help", "!help", False)[0].startswith("Welcome to Frytherer"))
        self.assertTrue(dispatch_message("help", "help", False)[0].startswith("Welcome to Frytherer"))
        self.assertTrue(dispatch_message("help", "!help", True)[0].startswith("Welcome to Frytherer"))

    def testHelpSearch(self):
        self.assertTrue(dispatch_message("helpsearch", "!helpsearch", False)[0].startswith("All these options"))
        self.assertTrue(dispatch_message("helpsearch", "helpsearch", False)[0].startswith("All these options"))
        self.assertTrue(dispatch_message("helpsearch", "!helpsearch", True)[0].startswith("All these options"))

    def testUrl(self):
        #  TODO: FIX self.assertTrue(dispatch_message("url", "!url cr", False)[0].startswith("http://"))
        self.assertTrue(dispatch_message("url", "url cr", False)[0].startswith("http://"))
        #  self.assertTrue(dispatch_message("url", "!url cr", True)[0].startswith("http://"))
        # self.assertTrue(dispatch_message("url", "!url amtr 1.10", False)[0].startswith("http://"))
        # self.assertTrue(dispatch_message("url", "url amtr 1.10", False)[0].startswith("http://"))
        # self.assertTrue(dispatch_message("url", "!url amtr 1.10", True)[0].startswith("http://"))
        # Also !url mtr <section>
        # Also: !mtr <section>

    def testGetCard(self):
        # Single card that exists (single word)
        self.assertEqual(dispatch_message("island", "!island", False)[0], "Island\n\nBasic Land - Island")
        self.assertEqual(dispatch_message("island", "island", False)[0], "Island\n\nBasic Land - Island")
        self.assertEqual(dispatch_message("island", "!island", True)[0], "*Island* |Basic Land - Island|")

        # Single card that doesn't exist (single word)
        self.assertEqual(dispatch_message("fryland", "!fryland", False)[0], "")
        self.assertEqual(dispatch_message("fryland", "fryland", False)[0], "")
        self.assertEqual(dispatch_message("fryland", "!fryland", True)[0], "")

        # Weird formatting
        # FIX: To use fast search
        self.assertEqual(dispatch_message("\"island\"", "!\"island\"", False)[0], "Island\n\nBasic Land - Island")
        # FIX: To not fail
        # self.assertEqual(dispatch_message("\"island\"", "\"island\"", False)[0], "Island\n\nBasic Land - Island\n\n")
        # FIX: To use fast search
        self.assertEqual(dispatch_message("\"island\"", "!\"island\"", True)[0], "*Island* |Basic Land - Island|")
        # FIX: To use fast search
        self.assertEqual(dispatch_message("'island'", "!'island'", False)[0], "Island\n\nBasic Land - Island")

        # Single card that exists (multiple word)
        self.assertTrue(dispatch_message("privileged", "!privileged position", False)[0].startswith("Privileged Position"))
        # FIX: To not fail
        # self.assertTrue(dispatch_message("privileged", "privileged position", False)[0].startswith("Privileged Position"))
        self.assertTrue(dispatch_message("privileged", "!privileged position", True)[0].startswith("*Privileged Position"))

        # Single card that doesn't exist (multiple word)
        self.assertEqual(dispatch_message("frycanic", "!frycanic fryland", False)[0], "")
        self.assertEqual(dispatch_message("frycanic", "frycanic fryland", False)[0], "")
        self.assertEqual(dispatch_message("frycanic", "!frycanic fryland", True)[0], "")

        # # Multiple cards that exist (single word) -- <= five
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest", "!island !mountain !swamp !plains !forest", False)[0], u'Forest\n\nBasic Land - Forest\nIsland\n\nBasic Land - Island\nMountain\n\nBasic Land - Mountain\nPlains\n\nBasic Land - Plains\nSwamp\n\nBasic Land - Swamp')
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest", "island !mountain !swamp !plains !forest", False)[0]) > 50, u'Forest\n\nBasic Land - Forest\n\n\nIsland\n\nBasic Land - Island\n\n\nMountain\n\nBasic Land - Mountain\n\n\nPlains\n\nBasic Land - Plains\n\n\nSwamp\n\nBasic Land - Swamp\n\n')
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest", "!island !mountain !swamp !plains !forest", True)[0], u'*Forest* |Basic Land - Forest|\n*Island* |Basic Land - Island|\n*Mountain* |Basic Land - Mountain|\n*Plains* |Basic Land - Plains|\n*Swamp* |Basic Land - Swamp|')

        # # Multiple cards that exist (single word) -- exceeds five
        # self.assertEqual(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", True)[0][0], "6 results sent to PM")
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", True)[1][0]) > 50)
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "!island !mountain !swamp !plains !forest !Gigantoplasm", False)[0]) > 50)
        # self.assertTrue(len(dispatch_message("island !mountain !swamp !plains !forest !Gigantoplasm", "island !mountain !swamp !plains !forest !Gigantoplasm", False)[0]) > 50)

    def testGetCardExtend(self):
        self.assertTrue(len(dispatch_message("island extend", "!island extend", False)[0]) > 50)
        self.assertTrue(len(dispatch_message("island extend", "island extend", False)[0]) > 50)
        self.assertTrue(len(dispatch_message("island extend", "!island extend", True)[0]) > 50)
        self.assertEqual(dispatch_message("fryland extend", "!fryland extend", False)[0], "")
        self.assertEqual(dispatch_message("fryland extend", "fryland extend", False)[0], "")
        self.assertEqual(dispatch_message("fryland extend", "!fryland extend", True)[0], "")

    def testGetCardStar(self):
        # Cards are found
        self.assertTrue(len(dispatch_message("island*", "!island*", False)[0]) > 50)
        self.assertTrue(len(dispatch_message("island*", "island*", False)[0]) > 50)
        self.assertEqual(dispatch_message("island*", "!island*", True)[0][0], "9 results sent to PM")
        self.assertTrue(len(dispatch_message("island*", "!island*", True)[1][0]) > 50)

        # Cards aren't found
        self.assertEqual(dispatch_message("fryland*", "!fryland*", False)[0], "")
        self.assertEqual(dispatch_message("fryland*", "fryland*", False)[0], "")
        self.assertEqual(dispatch_message("fryland*", "!fryland*", True)[0], "")

        # Too many cards are found
        self.assertTrue(dispatch_message("Phyrexian*", "!Phyrexian*", False)[0].startswith("Too many cards to print"))
        self.assertTrue(dispatch_message("Phyrexian*", "Phyrexian*", False)[0].startswith("Too many cards to print"))
        self.assertTrue(dispatch_message("Phyrexian*", "!Phyrexian*", True)[0].startswith("Too many cards to print"))

        # Exactly one card is found
        self.assertEqual(dispatch_message("Phyrexian War Beast*", "!Phyrexian War Beast*", False)[0], u'Phyrexian War Beast\n{3}\nArtifact Creature - Beast\n3/4\nWhen Phyrexian War Beast leaves the battlefield, sacrifice a land and Phyrexian War Beast deals 1 damage to you.\n1 result/s')
        self.assertEqual(dispatch_message("Phyrexian War Beast*", "Phyrexian War Beast*", False)[0], u'Phyrexian War Beast\n{3}\nArtifact Creature - Beast\n3/4\nWhen Phyrexian War Beast leaves the battlefield, sacrifice a land and Phyrexian War Beast deals 1 damage to you.\n1 result/s')
        self.assertEqual(dispatch_message("Phyrexian War Beast*", "!Phyrexian War Beast*", True)[0], u'*Phyrexian War Beast* {3} |Artifact Creature - Beast| 3/4 When Phyrexian War Beast leaves the battlefield, sacrifice a land and Phyrexian War Beast deals 1 damage to you.')

        # Between 2 and 5 cards are found
        self.assertTrue("5 result/s" in dispatch_message("Phyrexian R*", "!Phyrexian R*", False)[0])
        self.assertTrue("5 result/s" in dispatch_message("Phyrexian R*", "Phyrexian R*", False)[0])
        self.assertTrue(len(dispatch_message("Phyrexian R*", "!Phyrexian R*", True)[0]) > 50)

    def testGetRules(self):
        # FIX: Parsing rules queries in PM when not starting specifically with !r
        self.assertEqual(dispatch_message("r", "!r 100.6b", False)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        # self.assertEqual(dispatch_message("r", "r 100.6b", False)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(dispatch_message("100.6b", "100.6b", False)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        # self.assertEqual(dispatch_message("!100.6b", "!100.6b", False)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(dispatch_message("r", "!r 100.6b", True)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(dispatch_message("r", "!r Locator", False)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(dispatch_message("r", "!r Locator", False)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(dispatch_message("r", "!r Locator", True)[0], "100.6b: Players can use the Magic Store & Event Locator at Wizards.com/Locator to find tournaments in their area.\n")
        self.assertEqual(dispatch_message("r", "!r Fry", False)[0], "No rule/s found")
        self.assertEqual(dispatch_message("r", "!r Fry", True)[0], "No rule/s found")

    def testDoAdvancedSearch(self):
        self.assertEqual(dispatch_message("s en:\"Island\"", "!s en:\"Island\"", False)[0], "Island\n\nBasic Land - Island\n1 result/s")
        # FIX: Recognise advanced search in PM with no !
        # self.assertEqual(dispatch_message("s en:\"Island\"", "s en:\"Island\"", False)[0], "Island\n\nBasic Land - Island\n\n\n1 result/s")
        self.assertEqual(dispatch_message("s en:\"Island\"", "!s en:\"Island\"", True)[0], "*Island* |Basic Land - Island|")
        # FIX: Single quoted strings
        # self.assertEqual(dispatch_message("s en:'Island'", "!s en:'Island'", False)[0], "Island\n\nBasic Land - Island\n\n\n1 result/s")
        self.assertEqual(dispatch_message("s en:Island or en:Mountain and not en:Swamp", "!s en:Island or en:Mountain and not en:Swamp", False)[0], "Island\n\nBasic Land - Island\nMountain\n\nBasic Land - Mountain\n2 result/s")
        # self.assertEqual(dispatch_message("s en:Island or en:Mountain and not en:Swamp", "s en:Island or en:Mountain and not en:Swamp", False)[0], "Island\n\nBasic Land - Island\n\n\nMountain\n\nBasic Land - Mountain\n\n\n2 result/s")
        self.assertEqual(dispatch_message("s en:Island or en:Mountain and not en:Swamp", "!s en:Island or en:Mountain and not en:Swamp", True)[0], "*Island* |Basic Land - Island|\n*Mountain* |Basic Land - Mountain|")
        self.assertTrue(len(dispatch_message("s banned:vintage and legal:freeform", "!s banned:vintage and legal:freeform", False)[0]) > 50)
        # self.assertTrue(len(dispatch_message("s banned:vintage and legal:freeform", "!s banned:vintage and legal:freeform", False)[0]) > 50)
        self.assertEqual(dispatch_message("s banned:vintage and legal:freeform", "!s banned:vintage and legal:freeform", True)[0][0], "13 results sent to PM")
        self.assertTrue(len(dispatch_message("s banned:vintage and legal:freeform", "!s banned:vintage and legal:freeform", True)[1][0]) > 50)

        # Test brackets and implicit AND
        self.assertTrue(dispatch_message("s f:modern (n:Cryptic and t:Instant)", "!s f:modern (n:Cryptic and t:Instant)", False)[0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("s f:modern n:Cryptic t:Instant", "!s f:modern n:Cryptic t:Instant", False)[0].startswith("Cryptic Command"))

        # Should be failures
        self.assertTrue(dispatch_message("s n=Island", "!s n=Island", False)[0].startswith("Unable to parse search terms"))
        self.assertEqual(dispatch_message("s n:Fryland", "!s n:Fryland", False)[0], "No cards found")

    def testDoAdvancedSearchQuick(self):
        self.assertEqual(dispatch_message("qs en:\"Island\"", "!qs en:\"Island\"", False)[0], "Island ()\n1 result/s")
        # FIX: Recognise advanced search in PM with no !
        # self.assertEqual(dispatch_message("s en:\"Island\"", "s en:\"Island\"", False)[0], "Island\n\nBasic Land - Island\n\n\n1 result/s")
        self.assertEqual(dispatch_message("qs en:\"Island\"", "!qs en:\"Island\"", True)[0], "Island ()")
        # FIX: Single quoted strings
        # self.assertEqual(dispatch_message("s en:'Island'", "!s en:'Island'", False)[0], "Island\n\nBasic Land - Island\n\n\n1 result/s")
        self.assertEqual(dispatch_message("qs en:Island or en:Mountain and not en:Swamp", "!qs en:Island or en:Mountain and not en:Swamp", False)[0], "Island ()\nMountain ()\n2 result/s")
        # self.assertEqual(dispatch_message("s en:Island or en:Mountain and not en:Swamp", "s en:Island or en:Mountain and not en:Swamp", False)[0], "Island\n\nBasic Land - Island\n\n\nMountain\n\nBasic Land - Mountain\n\n\n2 result/s")
        self.assertEqual(dispatch_message("qs en:Island or en:Mountain and not en:Swamp", "!qs en:Island or en:Mountain and not en:Swamp", True)[0], "Island ()\nMountain ()")
        self.assertTrue(len(dispatch_message("qs banned:vintage and legal:freeform", "!qs banned:vintage and legal:freeform", False)[0]) > 50)
        # self.assertTrue(len(dispatch_message("s banned:vintage and legal:freeform", "!s banned:vintage and legal:freeform", False)[0]) > 50)
        self.assertEqual(dispatch_message("qs banned:vintage and legal:freeform", "!qs banned:vintage and legal:freeform", True)[0][0], "13 results sent to PM")
        self.assertTrue(len(dispatch_message("qs banned:vintage and legal:freeform", "!qs banned:vintage and legal:freeform", True)[1][0]) > 50)

        self.assertTrue(dispatch_message("qs f:modern (n:Cryptic and t:Instant)", "!qs f:modern (n:Cryptic and t:Instant)", False)[0].startswith("Cryptic Command"))
        self.assertTrue(dispatch_message("qs f:modern n:Cryptic t:Instant", "!qs f:modern n:Cryptic t:Instant", False)[0].startswith("Cryptic Command"))

        # Should be failures
        self.assertTrue(dispatch_message("qs n=Island", "!qs n=Island", False)[0].startswith("Unable to parse search terms"))
        self.assertEqual(dispatch_message("qs n:Fryland", "!qs n:Fryland", False)[0], "No cards found")

    def testGetRandomCard(self):
        self.assertTrue(len(dispatch_message("random", "!random", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("random", "random", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("random", "!random", True)[0]) > 5)

    def testPrintSets(self):
        self.assertTrue(len(dispatch_message("printsets", "!printsets", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("printsets", "printsets", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("printsets", "!printsets", True)[0]) > 5)

    def testPrintSetsInOrder(self):
        self.assertTrue(len(dispatch_message("printsetsinorder", "!printsetsinorder", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("printsetsinorder", "printsetsinorder", False)[0]) > 5)
        self.assertTrue(len(dispatch_message("printsetsinorder", "!printsetsinorder", True)[0]) > 5)


if __name__ == '__main__':
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')
    logging.basicConfig(level=logging.DEBUG)

    unittest.main()
