#!/usr/bin/python
#Here we will test while loops
#fundamental of while loops are same as if
# while <condition>:
#   statments
# we have to make sure that condition is false sometimes.
from sys import argv

def rangeMake(start,interval,max):
    number = start
    numbers = []
    while number < max:
        numbers.append(number)
        number = number + interval
    return numbers

script, start, interval, max = argv

numbers = rangeMake(int(start),int(interval),int(max))
sum = 0

for n in numbers:
    sum=sum+n
    print "%s " % n

print ""
print "%s" % sum