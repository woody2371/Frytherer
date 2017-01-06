from bs4 import BeautifulSoup
import datetime, pickle
import sys
sys.setrecursionlimit(10000)

stores = {}

for f in ['/tmp/events.html', '/tmp/events2.html']:
    soup = BeautifulSoup(open(f), "lxml")
    counter = 0
    for tr in soup.find_all('tr'):
        counter += 1
        if counter == 1:
            continue

        (eventdate, link, store, event, feeds, format) = tr.find_all('td')
        links = event.find_all('a')
        if links:
            event_link = links[0].get('href')
        else:
            event_link = None
        store_name = (store.string).lower().replace(" - ", " ").replace("premier organizer ", "")
        if store_name not in stores:
            stores[store_name] = []
        dt = datetime.datetime.strptime(eventdate.string, "%a %d %b")
        dt = dt.replace(year=datetime.date.today().year)
        if dt.month < datetime.date.today().month:
            dt = dt.replace(year=dt.year + 1)
        stores[store_name].append({'date': dt, 'event': event.text.encode('ascii', 'ignore').strip(), 'feeds': feeds.string, 'format': format.string, 'event_link': event_link})

pickle.dump(stores, open('events.obj', 'w'))

print stores.keys()
