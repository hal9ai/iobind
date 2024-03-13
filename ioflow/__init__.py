import sys

_RELEASE = False

argvidx = 1

def input(name):
	global argvidx
	value = sys.argv[argvidx]
	argvidx = argvidx + 1
	return value

def output(name, value):
	return
