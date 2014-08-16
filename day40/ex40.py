#!/usr/bin/python
class Song(object):
    def __init__(self, song,words):
        self.song = song
        self.words = words
    
    def whoAreYou(self):
        print self.song

    def sing(self):
        for line in self.words:
            print line


s = Song("One fine morning...",["One fine morning",
                                "When this life is over",
                                "I'll fly away...."])
s.whoAreYou()
q = raw_input("Want to sing me?: Y/N > ")
if q == "Y":
    s.sing()
else:
    print "No worries...!!"
