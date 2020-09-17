from pprint import pprint
# ex 33
import calendar
print(calendar.isleap(1900))


# ex 34
from datetime import date, timedelta, time, datetime

halloween = date(2020, 10, 31)
print(halloween.day, halloween.month, halloween.year, halloween.isoformat())

this_day = date.today()
one_day = timedelta(days=1)
tomorrow = this_day + one_day
pprint(tomorrow)
pprint(this_day + 17*one_day)

noon = time(12, 0, 0)

now = datetime.now()
print(now.microsecond)

noon_today = datetime.combine(this_day, noon)


# ex 35
import time

now = time.time()
print(now, time.ctime(now))
t = time.localtime()
fmt = "it's %A, %B %d, %Y, local time %I:%M:%S%p"
print(time.strftime(fmt, t))

fmt_t = "%Y-%m-%d"
#print(time.strftime("2012 0 1 29", fmt_t))


# ex 36
now = datetime.now()
with open("today.txt", 'w') as f:
    f.write(str(now))

with open("today.txt", 'r') as f:
    today_string = f.read()

print(today_string)


# ex 37
import os

print(os.listdir())
print(os.listdir('..'))


# ex 38
import multiprocessing
from random import randint
from time import sleep

def func(num:int) -> None:
    print(f'Start of Process {num}')
    sleep(randint(1, 5))
    print(f'End of Process {num}')


# ex 39
my_bday = date(1990, 6, 17)
print(my_bday, my_bday.weekday())
days10k = timedelta(days=1e4)
print(my_bday + days10k)


if __name__ == '__main__':
    for i in range(1, 4):
        p = multiprocessing.Process(target=func, args=(i,))
        p.start()

