#!/usr/bin/env python
#Example A3: Loop
#Python Crash Course
#dzul.aiman@gmail.com
#2015/12/08

def nested_loop():
    for x in xrange(1, 11):
        for y in xrange(1, 11):
            print '%d * %d = %d' % (x, y, x*y)

def early_exit():
    for x in xrange(3):
        if x == 1:
            break

def for_else():
    for x in xrange(3):
        print x
    else:
        print 'Final x = %d' % (x)

def iterable_string():
    string = "Hello World"
    for x in string:
        print x

def iterable_list():
    collection = ['hey', 5, 'd']
    for x in collection:
        print x

