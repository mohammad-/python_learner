#!/usr/bin/python
#This demostrates reading, writing and truncating files
#Let's read a file first.
filename = raw_input("Enter the file name > ")
raw_input("Do you want to erase this files? Hit Enter to erase CTRL+C to cancle > ")

f = open(filename,'w')

f.truncate()

print "Now we will write three lines in same file"
line1 = raw_input("line 1 > ")
line2 = raw_input("line 2 > ")
line3 = raw_input("line 3 > ")

formatter = "%s\n%s\n%s\n" % (line1,line2,line3)
f.write(formatter)

f.close()
print "file %s was written to drive" % filename
