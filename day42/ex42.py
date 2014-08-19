#!/usr/bin/python
print "Working with OOPs"
print "Little more of inheritance"
print "=="*10
class Person(object):
	def __init__(self,name):
		self.name = name	

class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name)
		self.salary = salary
	def introduction(self):
		return "I am %s" % self.name	


class Pet(object):
	def __init__(self,name):
		self.name = name

class Dog(Pet):
	def __init__(self,name,owner = None):
		super(Dog,self).__init__(name)
		self.owner = owner
	
	def introduction(self):
		if self.owner == None:
			return "I am %s and I am free...!!!" % (self.name)
		else:
			return "I am %s and my owner is %s" % (self.name,self.owner.name)		
		


e = Employee("Mohammad",120000)
print e.introduction()

p = Dog("J",e)
print p.introduction()

q = Dog("D")
print q.introduction()