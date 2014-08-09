#!/usr/bin/python
people = 10
dogs = 5
cats = 6

if people > dogs:
    print "too many owner for few dogs"

if people > cats:
    print "too many owner for cats"

if (cats + dogs) > people:
    print "too many pets for people"

#this will not be printed
if cats < dogs:
    print "too few cats here...."

people+=1

if (cats + dogs) == people:
    print "if one more guy is invited then it will be easy..."
