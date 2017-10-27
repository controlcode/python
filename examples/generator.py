#!/usr/bin/python

def func(x,y):
	for i in range(10):	
		yield x + y
		x += 1

for n in func(3, 2):
	print n
