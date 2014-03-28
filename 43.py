#!/usr/bin/python

def pandigital(num):
    count = {}
    if len(str(num)) != 10:
        return False
    for c in str(num):
        if count.has_key(c):
            return False
        else:
            count[c] = 1
    return True

def check(num):
    s = str(num)
    if int(s[1:3]) % 2 != 0:
        return 0
    if int(s[2:4]) % 3 != 0:
        return 0
    if int(s[3:5]) % 5 != 0:
        return 0
    if int(s[4:6]) % 7 != 0:
        return 0
    if int(s[5:7]) % 11 != 0:
        return 0
    if int(s[6:8]) % 13 != 0:
        return 0
    if int(s[7:9]) % 17 != 0:
        return 0
    return num

if __name__ == "__main__":

    t = 0

    for i in xrange(1000000000,10000000000):
        if pandigital(i) == True:
            t += check(i)

    print t
