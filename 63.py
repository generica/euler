#!/usr/bin/python

if __name__ == "__main__":

    tally = 0

    for pow in xrange(0, 32):
        for i in xrange(1, 15):
            x = i ** pow
            if len(str(x)) == pow:
                tally += 1
            elif len(str(x)) > pow:
                break

    print tally
