# pip install redis
import redis

conn = redis.Redis()

conn.set('secret', 'ni!')
conn.set('carats', 24)
conn.set('fever', '101.5')

print(conn.get('secret'))

conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')  # failed cause 'secret'
# key already exists
conn.setnx('havnot', 'do-od')

print(conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing'))
print(conn.get('secret'))
print(conn.getrange('secret', -6, -1))  # b'boing!'
conn.setrange('secret', 0, 'ICKY')
print(conn.get('secret'))

conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
print(conn.mget(['fever', 'carats']))

conn.delete('fever')

conn.incr('carats')
conn.incr('carats', 10)

conn.decr('carats')
conn.decr('carats', 15)

conn.set('fever', '101.5')


# lists
conn.lpush('zoo', 'bear')   # start
#conn.lpush('zoo', 'alligator', 'duck')  # start few elements

conn.linsert('zoo', 'before', 'bear', 'beaver')  # insert before bear
conn.linsert('zoo', 'after', 'bear', 'cassowary')   # insert after bear

conn.lset('zoo', 2, 'marmoset')   # insert on index
conn.rpush('zoo', 'yak')  # insert to the end of the list

print(conn.lindex('zoo', 3))  # get element by index
print(conn.lrange('zoo', 0, 10))

conn.ltrim('zoo', 1, 4)
conn.lrange('zoo', 0, -1)


# hash
conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})
conn.hset('song', 'mi': 'a note to follow re')

print(conn.hget('song', 'mi'))
print(conn.hmget('song', 're', 'do'))
print(conn.hkeys('song'))
print(conn.hvals('song'))
print(conn.hlen('song'))
print(conn.hgetall('song'))

conn.hsetnx('song', 'fa', 'a note that rhymes with la')


# sets
conn.sadd('zoo', 'duck', 'goat', 'turkey')
print(conn.scard('zoo')) # count
print(conn.smembers('zoo')) # all elements

conn.srem('zoo', 'turkey') # delete element

conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')

print(conn.sinter('zoo', 'better_zoo'))  # intersection
conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo')  # intersection saved to fowl_zoo
print(conn.smembers('fowl_zoo'))

print(conn.sunion('zoo', 'better_zoo')) # union
conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo') # union saved to fabulous_zoo
print(conn.smembers('fabulous_zoo'))

print(conn.sdiff('zoo', 'better_zoo'))  # 
