#!/usr/bin/python
#This time we explore more functions from file
#seek -> to move to position
#readline -> to read one line
#read -> read all data
#open -> to open a file
#and we user all this in functions

from sys import argv
script,filename = argv
 
def printAll(f):
	print f.read()

def printOneLine(count,f):
	print "line %s -> %s" % (count,f.readline())

def rewind(f):
	f.seek(0)

#open file
f = open(filename)

print "Printing all -----------------"
printAll(f)
print "rewind ----------------"
rewind(f)
print "line by line --------------"
printOneLine(1, f)
printOneLine(2, f)

