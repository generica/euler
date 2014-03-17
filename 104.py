#!/usr/bin/python

fibstore = {}

def pandigital(num):
    count = {}
    if len(str(num)) != 9:
        return False
    if '0' in num:
        return False
    for c in str(num):
        if count.has_key(c):
            return False
        else:
            count[c] = 1
    return True

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n in fibstore:
        return fibstore[n]
    else:
        f1 = fib(n - 1)
        fibstore[n - 1] = f1
        f2 = fib(n - 2)
        fibstore[n - 2] = f2

    return (f1 + f2)

if __name__ == "__main__":

    for n in range(1, 500000):
        f = fib(n)
        if len(str(f)) > 9:
            if pandigital(str(f)[:9]):
                print "Got at start of %s" % (n)
                if pandigital(str(f)[-9:]):
                    print "Got at end of %s [%s]" % (n, f)
                    break
