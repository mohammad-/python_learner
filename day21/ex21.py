#!/usr/bin/python
#This time we use function to return something
#We make a function to convert celsius to fahrenheit and vice versa
def c_to_f(value):
	print "converting %s into fahrenheit" % value
	return (value * 9/5) + 32

def f_to_c(value):
	print "converting into %s into celsius" % value
	return (value - 32) * 5/9

value1 = c_to_f(10)
print "10 celsius is %s fahrenheit" % value1
value2 = f_to_c(value1)
print "%s fahrenheit is %s celsius" % (value1,value2)

#Just to demostrate that function can be called from inside
print "10 celsius to fahrenheit and back \n", f_to_c(c_to_f(10)) 
