#!/usr/bin/python

if __name__ == "__main__":

    tally = 0
    curpos = 1
    step = 10
    points = []

    for i in xrange(1, 200000):
        numdigits = len(str(i))
        if tally + numdigits == curpos:
            points.append(int(str(i)[0]))
            curpos *= step
        elif tally + numdigits >= curpos:
            points.append(int(str(i)[curpos - tally - 1]))
            curpos *= step
        tally += numdigits

    p = 1

    for point in points:
        p *= point

    print p
