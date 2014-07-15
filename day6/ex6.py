#!/usr/bin/python
name = 'James '
surname = 'Bond'
fullname = "My name is %s, %s" % (surname,name+surname)
print fullname
print "Looks like you didn'h heard that. I said %r" % fullname
year = 1980
month = 6
day = 27
birthday = "%d/%d/%d"%(day,month,year)
father = "Ian Fleming"
print "I was born on %s. %s is my father" % (birthday,father)


