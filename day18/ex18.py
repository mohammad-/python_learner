#!/usr/bin/python
#This demostrates function in python
#Syntex for function is def <Name>(<args>):

def printTwo(*args):
	arg1,arg2 = args
	print "arg1 %s, arg2 %s" % (arg1,arg2)

def printTwoSimple(arg1,arg2):
	print "arg1 %s, arg2 %s" % (arg1,arg2)

def printOne(arg):
	print "arg %s" % arg

def printNone():
	print "Simple Print"

printNone()
printOne("One")
printTwoSimple("One","Two")
printTwo("OneX","TwoX")


