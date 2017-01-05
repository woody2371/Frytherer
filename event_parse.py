from bs4 import BeautifulSoup
import datetime, pickle
import sys
sys.setrecursionlimit(10000)

stores = {}

soup = BeautifulSoup(open('/tmp/events.html'), "lxml")
counter = 0
for tr in soup.find_all('tr'):
    counter += 1
    if counter == 1:
        continue

    (eventdate, link, store, event, feeds, format) = tr.find_all('td')
    if store.string not in stores:
        stores[store.string] = []
    dt = datetime.datetime.strptime(eventdate.string, "%a %d %b")
    dt = dt.replace(year=datetime.date.today().year)
    if dt.month < datetime.date.today().month:
        dt = dt.replace(year=dt.year + 1)
    stores[store.string].append({'date': dt, 'event': event.text.encode('ascii', 'ignore').strip(), 'feeds': feeds.string, 'format': format.string})

pickle.dump(stores, open('events.obj', 'w'))
