#!/usr/bin/python

fibstore = {}

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

    f = 0
    i = 0
    sum = 0

    while f < 4000000:
        i += 1
        f = fib(i)
        if (f % 2) == 0:
            sum += f

    print sum
