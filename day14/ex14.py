#!/usr/bin/python
#This exercises intends to user 
#raw_input and argv together

from sys import argv
script, name = argv
print "Hi %s, this is %s",(name,script)
print "Let me ask you some question"
sport = raw_input("Which is your favourite sport? ")
player = raw_input("Who is your favourite player? ")
game = raw_input("Which one game of that player you think you would like to witness live? ")

print """
	So you love %s,
	and you admire %s,
	and you think you should have been in
	stadium when %s played %s
      """ % (sport,player,player,game)






