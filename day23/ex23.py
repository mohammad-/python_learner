#!/usr/bin/python
#Demostration of String function
#.split -> split string by delimeter
#sorted -> sorting
#pop -> take out first element, last element when argument is -1

def splitWords(line):
	return line.split(' ')

def sortIt(words):
	return sorted(words)

def popFirst(words):
	return words.pop(0)

def popLast(words):
	return words.pop(-1)

def breakAndSort(line):
	l = splitWords(line)
	return sortIt(l)
#open python cell and do import ex23
#then run following command in it
#l = ex23.splitWords("one two three four")
#m = ex23.sortIt(l)
#m
#ex23.popFirst(m)
#ex23.popLast(m)
#ex23.popFirst(breakAndSort("There you go!!"))

