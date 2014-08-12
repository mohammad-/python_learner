#!/usr/bin/python
file = open("data.txt")
data = file.read()
dataLines = data.split('\n')
birthMonth = int(raw_input("enter your birth month 1 ~ 12: "))
if 1<= birthMonth <= 12:
	line = dataLines.pop(birthMonth - 1)
	parts = line.split(":")
	print "So you were born in month of %s" % parts.pop(0)
	print "Following is rough prediction of your future\n %s" % parts.pop(0)
	print "\n\nThis horoscop is shit...." 
else:
	print "Print LOL you have no future"
