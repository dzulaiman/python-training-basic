#!/usr/bin/env python
#Example B3: Read/Write
#Python Crash Course
#dzul.aiman@gmail.com
#2015/12/08

def read(filename):
    fo = open(filename, "rb") 
    print "Name of the file: ", fo.name 
    print "Closed or not : ", fo.closed 
    print "Opening mode : ", fo.mode 
    print "Softspace flag : ", fo.softspace

    fread = fo.read()
    print "\n",fread

    fo.close()

read("u_ex110429.log")
