#!/usr/bin/python

if __name__ == "__main__":

    tally = 0

    for i in xrange(2, 1000000):
        sum = 0
        for digit in str(i):
            sum += int(digit) ** 5
        if sum == i:
            tally += i
            print "New tally: %d" % (tally)
