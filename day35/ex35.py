#!/usr/bin/python
#encoding=utf-8
#Play with a list.
import random

list = [1,2,3,4,5,6]
print list

#map a list
def m(x): return x**x
print map(m,list)

#reduce
def op(x,y): return x*y
print reduce(op,list)

#map to string
def i(x): return "%d" % x
print "->".join(map(i,list))

print "->".join(map(i,range(10)))

name = ['1','2','3','4','5','6','7','8','9','J','Q','K','A']
flavour = ['CLUB','DIMOND','HEART','SPADES']
deck = []
#make the deck
for f in flavour:
	for n in name:
		deck.append(f+" "+n)		
		
random.shuffle(deck)
print deck