import redis

conn = redis.Redis()

conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever'. '101.5')

print(conn.get('secret'))

conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')  # failed cause 'secret'
# key already exists
conn.setnx('havnot', 'do-od')

print(conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing'))

print(conn.getrange('secret', -6, -1))  # b'boing!'
