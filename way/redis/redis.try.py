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


# redis lists
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


# redis hash
conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})
conn.hset('song', 'mi', 'a note to follow re')

print(conn.hget('song', 'mi'))
print(conn.hmget('song', 're', 'do'))
print(conn.hkeys('song'))
print(conn.hvals('song'))
print(conn.hlen('song'))
print(conn.hgetall('song'))

conn.hsetnx('song', 'fa', 'a note that rhymes with la')


# redis sets
conn.sadd('zoo2', 'duck', 'goat', 'turkey')
print(conn.scard('zoo2')) # count
print(conn.smembers('zoo2')) # all elements

conn.srem('zoo2', 'turkey') # delete element

conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')

print(conn.sinter('zoo2', 'better_zoo'))  # intersection
conn.sinterstore('fowl_zoo', 'zoo2', 'better_zoo')  # intersection saved to fowl_zoo
print(conn.smembers('fowl_zoo'))

print(conn.sunion('zoo2', 'better_zoo')) # union
conn.sunionstore('fabulous_zoo', 'zoo2', 'better_zoo') # union saved to fabulous_zoo
print(conn.smembers('fabulous_zoo'))

print(conn.sdiff('zoo2', 'better_zoo'))  # subtract of sets
conn.sdiffstore('zoo_sale', 'zoo2', 'better_zoo') # subtract saved to zoo_sale
print(conn.smembers('zoo_sale'))


# redis ordered sets
from time import time, sleep

now = time()

conn.zadd('logins', {'smeagol': now})
conn.zadd('logins', {'sauron': now + (5*60)})
conn.zadd('logins', {'bilbo': now + (2*60*60)})
conn.zadd('logins', {'treebeard': now + (24*60*60)})

print(conn.zrank('logins', 'bilbo'))   # index of 'bilbo' in 'logins'
print(conn.zscore('logins', 'bilbo'))  # timestamp of 'bilbo'

print(conn.zrange('logins', 0, -1))    # all elements ordered
print(conn.zrange('logins', 0, -1, withscores=True))  # dicts of elements


# redis bits
days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

conn.setbit(days[0], big_spender, 1)
conn.setbit(days[0], tire_kicker, 1)
conn.setbit(days[1], big_spender, 1)
conn.setbit(days[2], big_spender, 1)
conn.setbit(days[2], late_joiner, 1)

#for day in days:
#    print(conn.bitcount(day))  # overall count

print(conn.getbit(days[1], tire_kicker))  # is tire_kiker in days[1]

#conn.bitop('and', 'everyday', *days)  # 'everyday' creation
#print(conn.bitcount('everyday'))  # how many users login everyday
print(conn.getbit('everyday', big_spender))

#conn.bitop('or', 'alldays', *days)  # 'alldays' creation
#conn.bitcount('alldays')  # unique users overall


# temporal cache
key = 'now you see it'
conn.set(key, 'but not for long')
conn.expire(key, 5)
print(conn.ttl(key))  # life duration of key
print(conn.get(key))
sleep(6)
print(conn.get(key))
