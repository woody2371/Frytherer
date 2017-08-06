# -*- coding: utf-8 -*-
"""Pull the spoiler RSS feed from MTGSalvation and attempt to scrape
the list of cards from it, then add new cards to the database"""
import feedparser
import pysqlite2.dbapi2 as sqlite
import sys

# Create table if it doesn't exist, and connect to db
try:
    conn = sqlite.connect('frytherer.db', check_same_thread=False)
    conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
    conn.row_factory = sqlite.Row
    c = conn.cursor()
except sqlite.OperationalError:  # pragma: no cover
    print "Unable to open database - goodbye"
    sys.exit(0)
c.execute('''CREATE TABLE IF NOT EXISTS spoilers (
                name TEXT PRIMARY KEY UNIQUE,
                'text' TEXT,
                type TEXT,
                rarity TEXT,
                'set' TEXT,
                manaCost TEXT,
                flavor TEXT,
                artist TEXT,
                setnum TEXT
                );
''')

# Pull the RSS feed as a dict
d = feedparser.parse('http://www.mtgsalvation.com/spoilers.rss')
# A list of card dictionaries for easier searching later check if parsing successful
if d["status"] == 200:
    for entry in d['entries']:
        # Iterate through the card entries and create a card dictionary in the same format as it is stored in the database
        card = {"text": "", "flavor": ""}
        # Rules can be multiple lines, so this flag tells us if we are currently inside that paragraph
        ruleFlag = 0
        skipFlag = 0
        ruleString = ""
        for value in entry['summary_detail']['value'].replace("<b>", "").replace("</b>", "").replace("<br />", "").split("\n"):
            # Check if we're currently in the rules text
            if ruleFlag == 1:
                if not (value.startswith("Flavor Text:") or value.startswith("Illus.")):
                    if value:
                        ruleString += value + " / "
                else:
                    ruleFlag = 0
            if value.startswith("Name:"):
                # Check if we already have this card
                card_check = c.execute("SELECT * FROM spoilers WHERE name = ?", (value[6:],)).fetchall()
                if card_check:
                    print 'Skipping {}'.format(value[6:].encode('utf-8'))
                    skipFlag = 1
                    break
                card["name"] = value[6:]
            elif value.startswith("Set:"):
                card["set"] = value[5:]
            elif value.startswith("Cost:"):
                card["manaCost"] = value[6:]
            elif value.startswith("Type:"):
                card["type"] = value[6:]
            elif value.startswith("Rules Text:"):
                ruleFlag = 1
                ruleString += value[12:] + " "
            elif value.startswith("Flavor Text:"):
                card["flavor"] = value[13:]
            elif value.startswith("Illus."):
                card["artist"] = value[7:]
            elif value.startswith("Rarity:"):
                card["rarity"] = value[8:]
            elif value.startswith("Set Number:"):
                card["setnum"] = value[13:]
        # Strip off final newline and save rulestext
        card["text"] = ruleString.replace("<i>", "_").replace("</i>", "_").strip(" / ")
        if skipFlag == 0:
            c.execute("INSERT INTO spoilers(name, 'text', 'set', manaCost, type, flavor, artist, rarity, setnum) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", (card["name"], card["text"], card["set"], card["manaCost"], card["type"], card["flavor"], card["artist"], card["rarity"], card["setnum"]))
        skipFlag = 1
else:
    print("Error pulling the RSS feed")
    sys.exit(0)

conn.commit()
