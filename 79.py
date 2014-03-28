#!/usr/bin/python

import sys

keys = open('keylog.txt', 'r').readlines()

def contains(passcode, chars):

    start = 0

    for char in chars:
        found = passcode.find(char, start)
        if found == -1:
            return False
        start = found

    return True

def check(passcode):

    for key in keys:
        if contains(passcode, key.strip()) == False:
            return False

    print "%s" % (passcode)
    sys.exit(0)

if __name__ == "__main__":

    for i in xrange(1, 10000000000):
        check(str(i))
