#!/usr/bin/python
#Lets work with some pure logical statments
#and operators
#each print statment prints logic result of following statments

print True and False

print True and (0 == 0)
print True or (0 == 0)

print 1 == 1 and True

print 1 == 1 and False

print "test" == "test"

one = "test"
two = "test"

print one == two
print one != two

print "test" == "testing"

print not True
print not False

print not(one == two)

print 10 > 20

var = 10 > 30
print var

def compare(a,b):
    print "comparing ",a," with ",b
    return a == b

print compare(10,10)
print compare(12,10)

#note that compare is not called here
print False and compare(10,10)

#both comapres are called here
print compare(30,30) and compare(10,20)

#note that compare is not called here too
print True or compare(10,10)

#and only one compare here
print compare(10,10) or compare(10,10)