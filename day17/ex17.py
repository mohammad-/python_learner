#!/usr/bin/python
# This demostrats more file operations
# We will copy data from one file to another
# Other than that we will use some more functions
# like len() and exists() to check file lenght and 
# weather file exists of not.
from os.path import exists

infile = raw_input("Enter source file name > ")
outfile = raw_input("Enter output file name > ")

print "Source file exists? %r" % exists(infile)
print "Output file exists? %r" % exists(outfile)
print "Reading Source file..."

inF = open(infile)
data = inF.read()
print "lenght of input file is %r bytes" % len(data)

raw_input("Are you sure you want to copy this data?\nEnter to continue\nCTRL+C to abort > ")

out = open(outfile,'w')
out.write(data)
out.close()
inF.close()

print("All Done...")
