#!/usr/bin/python
#one function can return many things.
#we can assign it same way as argv
#This function will return many things
def manyReturn(start):
	st = "start is %s" % start
	mt = "start multiply by 10 is %s " % (start*10)
	return st,mt

#this will catch many things returned by function
st,mt = manyReturn(10)
#this will print that
print "%r and %r " % (st,mt)
