#!/usr/bin/python
# This program is to demostrate for loops
# and lists

numbers = [1,2,3,4,5]
fruits = ["apple","orange","banana","cherry"]
countries = ["india","japan","france","england","usa"]

for n in numbers:
    print n

for fruit in fruits:
    print fruit

for country in countries:
    print country

#lets now build a list

list = []
for i in range(1,10):
    if i % 2:
        list.append(i)

print "following are odd numbers between 1~10"
for i in list:
    print i

