#!/usr/bin/python

import itertools

c = 0
s = ""

for i in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    c += 1
    if c == 1000000:
        for d in i:
            s = "%s%d" % (s, d)

print s
