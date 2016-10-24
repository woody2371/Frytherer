# -*- coding: utf-8 -*-
"""Import cards from JSON into SQLite DB."""

import pysqlite2.dbapi2 as sqlite
import sys, json

if __name__ == '__main__':
    try:
        conn = sqlite.connect('frytherer.db', check_same_thread=False)
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
        c.execute("DROP TABLE IF EXISTS sets")
        c.execute("DROP TABLE IF EXISTS cards")
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
                        )""", (s['name'].encode('utf-8'), s['code'].encode('utf-8'), str(s.get('languagesPrinted', [])), s.get('releaseDate', '').encode('utf-8'), s.get('type', '').encode('utf-8'), s.get('magicCardsInfoCode', '').encode('utf-8'), s['border'].encode('utf-8'), s.get('block', '').encode('utf-8'), str(s.get('booster', []))))

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

    numCards = -1

    # Check if the database actually has stuff
    try:
        c.execute('SELECT COUNT(DISTINCT(name)) FROM hearthstonecards')
        numCards = c.fetchone()[0]
    except sqlite.OperationalError:
        print "No cards in DB? Trying to import"
        numCards = 0

    if numCards < 1:
        # Load in all the cards
        try:
            with open('cards.json') as data_file:
                hs_cards = json.load(data_file)
        except IOError:
            print "Unable to import cards - goodbye"
            sys.exit(0)
        c.execute("DROP TABLE IF EXISTS hearthstonecards")

        c.execute("""
            CREATE TABLE hearthstonecards (
                id TEXT PRIMARY KEY UNIQUE,
                name TEXT,
                text TEXT,
                rarity TEXT,
                type TEXT,
                cost NUMERIC,
                attack NUMERIC,
                health NUMERIC,
                'set' TEXT,
                artist TEXT,
                flavor TEXT,
                mechanics TEXT,
                race TEXT,
                durability NUMERIC
            )""")
        print len(hs_cards)
        for card in hs_cards:
            c.execute("""
                    INSERT INTO hearthstonecards VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                    )""", (card['id'], card['name']['enUS'], card.get('text', {}).get('enUS', ''), card.get('rarity', '').title(), card.get('type', '').title(), card.get('cost', 0), card.get('attack', 0), card.get('health', 0), card.get('set', ''), card.get('artist', ''), card.get('flavor', {}).get('enUS', ''), ', '.join(card.get('mechanics', [])), card.get('race', '').title(), card.get('durability', 0)))
        c.execute('CREATE INDEX hscardname ON hearthstonecards (name)')
        conn.commit()
