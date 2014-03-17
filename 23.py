#!/usr/bin/python

def get_divisors(n):

    d = []

    for x in range(1, int(n*0.5)+1):
        if n % x == 0:
            d.append(x)

    return d

def check(n):

    d = get_divisors(n)
    s = sum(d)
    if 

if __name__ == __main__:

    for i in range(1, 28124):
        sum += check(i)

    print sum
