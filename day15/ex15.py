#!/usr/bin/python
from sys import argv

script, filename = argv
txt = open(filename)
print "Here is content of %r" % filename
print txt.read()

file2 = raw_input("Enter file name > ")
txt = open(file2)
print txt.read()
