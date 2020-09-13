from random import random, randint

filename = 'gpsdata.csv'

def getdata(num):
    data = ""
    for i in range(num):
        data += ("%.2f,%.2f,speed=%i\n" % (random()*180,random()*180,randint(10,60)))
    return data

with open(filename, 'w') as file:
    file.write(getdata(100))

