import memcache

db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')
print(db.get('marco'))

db.set('ducks', 0)
print(db.get('ducks'))

db.incr('ducks', 2)
print(db.get('ducks'))
