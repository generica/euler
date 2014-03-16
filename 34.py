#!/usr/bin/python

facts = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

def compute_fact(n):
    return facts[n]

if __name__ == "__main__":

    tally = 0

    for i in xrange(3, 10000000):
        sum = 0
        for digit in str(i):
            sum += compute_fact(int(digit))
        if sum == i:
            tally += i
            print "New tally: %d" % (tally)

