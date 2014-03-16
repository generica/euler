#!/usr/bin/python

tris = []
pens = []
hexs = []

def tri(n):
    return n * (n + 1) / 2

def pen(n):
    return n * (3 * n - 1) / 2

def hex(n):
    return n * (2 * n - 1)

if __name__ == "__main__":

    for i in xrange(1, 100000):
       tris.append(tri(i))
       pens.append(pen(i))
       hexs.append(hex(i))

    a = set(tris).intersection(set(pens)).intersection(set(hexs))
    print a
