# -*- coding: utf-8 -*-
"""Import cards from JSON into SQLite DB."""

import pysqlite2.dbapi2 as sqlite
import sys, json, pickle
try:
    from wow_db_data import *
except ImportError:
    print "No WOW data available"

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
        except IOError:
            print "Unable to import cards - goodbye"
            sys.exit(0)

    ##
    # Load WOW stuff
    ##

    # Chieves
    numCards = -1

    # Check if the database actually has stuff
    try:
        c.execute('SELECT COUNT(DISTINCT(id)) FROM wowchieves')
        numCards = c.fetchone()[0]
    except sqlite.OperationalError:
        print "No chieves in DB? Trying to import"
        numCards = 0

    if numCards < 1:
        # Load in all the chieves
        try:

            c.execute("DROP TABLE IF EXISTS wowchieves")
            c.execute("""
                CREATE TABLE wowchieves (
                    id TEXT PRIMARY KEY UNIQUE,
                    title TEXT,
                    faction NUMERIC,
                    description TEXT,
                    criteria TEXT
            )""")
            for x in wow_chieves["achievements"]:
                if len(x.get("categories", [])):
                    for cat in x["categories"]:
                        for chieve in cat["achievements"]:
                            c.execute("""
                                INSERT INTO wowchieves VALUES (
                                    ?, ?, ?, ?, ?
                                )""", (chieve["id"], chieve["title"], chieve["factionId"], chieve.get("description", ""), str(chieve["criteria"])))
                if len(x.get("achievements", [])):
                    for chieve in x["achievements"]:
                            c.execute("""
                                INSERT INTO wowchieves VALUES (
                                    ?, ?, ?, ?, ?
                                )""", (chieve["id"], chieve["title"], chieve["factionId"], chieve.get("description", ""), str(chieve["criteria"])))
            c.execute('CREATE INDEX chievename ON wowchieves (id)')
            conn.commit()
        except:
            print "Unable to import chieves"
            print sys.exc_info()

    # Realms
    numCards = -1

    # Check if the database actually has stuff
    try:
        c.execute('SELECT COUNT(DISTINCT(name)) FROM wowrealms')
        numCards = c.fetchone()[0]
    except sqlite.OperationalError:
        print "No realms in DB? Trying to import"
        numCards = 0

    if numCards < 1:
        # Load in all the realms
        try:
            from wow_db_data import *
            c.execute("DROP TABLE IF EXISTS wowrealms")
            c.execute("""
                CREATE TABLE wowrealms (
                    name TEXT PRIMARY KEY UNIQUE,
                    type TEXT,
                    locale TEXT,
                    timezone TEXT,
                    connected_realms TEXT

            )""")
            for x in wow_realms["realms"]:
                c.execute("""
                    INSERT INTO wowrealms VALUES (
                        ?, ?, ?, ?, ?
                )""", (x["name"], x["type"], x["locale"], x["timezone"], str(x["connected_realms"])))
            c.execute('CREATE INDEX realmname ON wowrealms (name)')
            conn.commit()
        except:
            print "Unable to import realms"
            print sys.exc_info()

    # Stats
    numCards = -1

    # Check if the database actually has stuff
    try:
        c.execute('SELECT COUNT(DISTINCT(name)) FROM wowstats')
        numCards = c.fetchone()[0]
    except sqlite.OperationalError:
        print "No stats in DB? Trying to import"
        numCards = 0

    if numCards < 1:
        # Load in all the stats
        try:
            c.execute("DROP TABLE IF EXISTS wowstats")
            c.execute("""
                CREATE TABLE wowstats (
                    name TEXT PRIMARY KEY UNIQUE
            )""")
            with open('wow_stats.obj', 'r') as f:
                stats = pickle.load(f)
            for stat in stats:
                c.execute("""
                    INSERT INTO wowstats VALUES (
                        ?
                )""", (stat,))
            c.execute('CREATE INDEX statname ON wowstats (name)')
            conn.commit()
        except:
            print "Unable to import stats"
            print sys.exc_info()
