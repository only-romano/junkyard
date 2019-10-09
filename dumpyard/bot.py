import lxml.html
import sqlite3
from urllib.request import urlopen
from urllib.parse import urlencode
from os import environ

html = urlopen(environ['KRISHAKZBOT_URL'], timeout=60).read().decode('utf-8')
doc = lxml.html.fromstring(html)
top_ads = [(link.get('href'),) for link in doc.cssselect('.a-card__title')]

conn = sqlite3.connect('krisha.db')
conn.execute('create table if not exists ad(url text)')
conn.execute('create temp table top_ad(url text)')
conn.executemany('insert into top_ad(url) values (?)', top_ads)
new_ads = conn.execute('select url from top_ad except select url from ad').fetchall()

for (url,) in new_ads:
    try:
        urlopen('https://api.telegram.org/bot' + environ['KRISHAKZBOT_TGBOTTOKEN'] + '/sendMessage?' + urlencode({
            'chat_id': environ['KRISHAKZBOT_TGCHATID'],
            'text': 'https://krisha.kz' + url,
        }), timeout=60)
    except Error as err:
        print(err)
    else:
        conn.execute('insert into ad(url) values(?)', (url,))

conn.commit()
