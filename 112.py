#!/usr/bin/python

def isbouncy(num):

    l = list(str(num))
    if l == sorted(l):
        return False
    m = sorted(l, reverse=True)
    if l == m:
        return False

    return True

if __name__ == "__main__":

    bouncy = 0

    for i in xrange(1,1000000000):
        if isbouncy(i) == True:
            bouncy += 1
        ratio = bouncy * 100 / i
        if ratio == 99:
            print i
            break
