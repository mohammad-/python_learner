#!/usr/bin/python
class Person(object):
    def __init__(self,name):
        self.name = name

    def whoAreYou(self):
        print "I am",self.name

class Officer(Person):
    def __init__(self,name,rank):
        super(Officer,self).__init__(name)
        self.rank = rank


    def whoAreYou(self):
        super(Officer,self).whoAreYou()
        print "I am officer and my Rank is",self.rank

class SalaryMan(Person):
    def __init__(self,name,salary):
        super(SalaryMan,self).__init__(name)
        self.salary = salary

    def whoAreYou(self):
        super(SalaryMan,self).whoAreYou()
        print "I am just another salary man struggling to make %s" % self.salary

class CEO(Person):
    def __init__(self,name,company):
        super(CEO,self).__init__(name)
        self.company = company
    
    def whoAreYou(self):
        super(CEO,self).whoAreYou()
        print "I am CEO at %s" % self.company


o = [Officer("A","O"),SalaryMan("X","Y"),CEO("One","Two")]
for x in o:
    x.whoAreYou()
    print "=" * 10
