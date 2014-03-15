#!/usr/bin/python

import sys

def check_pythag(a, b, c):

    if (a ** 2) + (b ** 2) == (c ** 2):
        print "Success! %d " % (a * b * c)
        sys.exit(0)

if __name__ == "__main__":

    for a in range(1, 1000):
       for b in range(1, 1000):
           for c in range(1, 1000):
               if (a == b) or (a == c) or (b == c):
                   break
               if (a + b + c) == 1000:
                   if (a > b) and (a > c):
                       check_pythag(b, c, a)
                   elif (b > c):
                       check_pythag(a, c, b)
                   else:
                       check_pythag(a, b, c)
