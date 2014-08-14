#!/usr/bin/python
#room game

def gold_room():
    print "You are in gold room"
    print "How many gold bars will you take",
    bars = int(raw_input("> "))
    if bars > 50:
        print "Don't go gridy my friend..."
    elif bars < 10:
        print "You should have taken more..."
    else:
        print "You played well..."

def animal_room():
    print "You are in front in of a bear..."
    option = int(raw_input("What will you do? \n#1 Take Right Door and Escape\n#2 Fight like a worrier\n>"))
    if option == 1:
            print "Good..."
            gold_room()
    else:
        print "Too much confidence is not good"
        print "We are done..."
        
def dark_room():
	print "Its a dark toom and you are stuck here...."
	print "There is no where to go...."
	
def puzzle_room():
    print "You are in a puzzle room"
    option = int(raw_input("What will you do? \n#1 Take Right Door \n#2 Take Left Door\n>"))
    if option == 1:
            print "Good..."
            animal_room()
    else:
		    print "Dark Room...."
		    dark_room()
		    
def start():
	print "Welcome to puzzle"
	puzzle_room()
	
start()			                
    
