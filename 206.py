#!/usr/bin/python

import re

def check(num):
    s = str(num)
    if not re.search('1.2.3.4.5.6.7.8.9.0', s):
        return False
    else:
        return True

if __name__ == "__main__":

    for i in xrange(1000000000, 100000000000, 10):
        x = i ** 2
        if len(str(x)) == 19:
            if check(x) == True:
                print i 
                break
