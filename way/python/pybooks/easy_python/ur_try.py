import urllib.request as ur

url = 'http://www.iheartquotes.com/api/v1/random'
conn = ur.urlopen(url)
data = conn.read()
print(conn, data, conn.status, conn.getheader('Content-Type'))

for key, value in conn.getheaders():
    print(key, value)
