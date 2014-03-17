#!/usr/bin/python

key = [103, 111, 100]
k = 0

def find_key():
    start = "79,59,12,2,79,35,8,28,20,2,3,68,8,9,68,45,0,12,9,67,68,4,7,5,23,27,1,21,79,85,78,79,85,71,38,10,71,27,12,2,79,6,2,8,13,9,1,13,9,8,68,19,7,1,71,56,11,21,11,68,6,3,22,2,14,0,30,79,1,31,6,23,19,10,0,73,79,44,2,79,19"
    letters = start.split(',')

    for a in xrange(97, 123):
        for b in xrange(97, 123):
            for c in xrange(97, 123):
                key = [a, b, c]
                test = []

                for letter in letters:   
                    test.append(chr(int(letter) ^ key[k]))
                    k += 1
                    if k > 2:
                        k = 0

                teststring = "".join(test)
                if "The" in teststring:
                    print key, teststring


full = open('cipher1.txt', 'r').read().split(',')
test = []
tally = 0

for letter in full:
    test.append(chr(int(letter) ^ key[k]))
    tally += int(letter) ^ key[k]
    k += 1
    if k > 2:
        k = 0

teststring = "".join(test)
print tally
