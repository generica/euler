#!/usr/bin/python

if __name__ == "__main__":

    tally = 0
    s = ""

    for i in xrange(1, 200000):
        numdigits = len(str(i))
        tally += numdigits
        s = "%s%d" % (s, i)
#        print i, numdigits, tally

    tot = int(s[999999]) * int(s[99999]) * int(s[9999]) * int(s[999]) * int(s[99]) * int(s[9]) * int(s[0])
    print tot
