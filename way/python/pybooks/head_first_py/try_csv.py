import csv
from pprint import pprint
from datetime import datetime

def proceed_time(time: str) -> str:
    hours, minutes = time.split(':')
    i_h = int(hours)
    end = 'AM' if i_h < 12 else 'PM'
    hours = f'{"0" if i_h < 22 else ""}{i_h-12}' if i_h > 12 else hours
    return f'{hours}:{minutes}{end}'


def proceed_destination(dest: str) -> str:
    return " ".join(map(lambda x: x.capitalize(), dest.split(' ')))


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


def time(line):
    time, _ = line.strip().split(',')
    return convert2ampm(time)

def dest(line):
    _, dest = line.strip().split(',')
    return dest.title()


with open('buzzers.csv') as data:
    data.readline()
    flights = { time(line) : dest(line) for line in data.readlines() }

destinations = {d: [t for t, m in flights.items() if m == d] for d in set(flights.values())}

pprint(flights)
pprint(destinations)
