from nntplib import NNTP_SSL
from datetime import date, timedelta

server_configure = {
    'host': 'news.free-usenet.com',
    'port': 443,
    'user':'U69417191015',
    'password':'PD9C486FA'
}

group = 'comp.lang.python.announce'

server = NNTP_SSL(server_configure['host'], 
    port=server_configure['port'],
    user=server_configure['user'],
    password=server_configure['password']
)

group = 'comp.lang.python.announce'
my_date = date.today() - timedelta(days=2)
server.group(group)
print(server.body("2432"))
#resp, groups = server.newgroups(date.today() - timedelta(days=2))
