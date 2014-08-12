#!/usr/bin/python
#This program demonstrates if elif and else conditions
# 1. take number form user as input
# 2. check if its > 100 => out of range
# 3. check if its < 0 => out if range 
# 4. check if its > 50 => bigger than 50
# 5. check if its < 50 => less than 50
# 6. check if its == 50 Oh! thats 50 

number = int(raw_input("Enter a number between 0~100: "))

if number > 100 or number < 0:
	print "%s is out of range" % number
else:
	if number > 50:
		print "This number is bigger than 50"
	elif number < 50:
		print "this number is less than 50"
	else:
		print "Oh!! this is 50"
	