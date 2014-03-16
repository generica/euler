#!/usr/bin/python

if __name__ == "__main__":

    sum = 0

    for i in xrange(1, 1001):
         sum += i ** i
         print str(sum)[-10:]
