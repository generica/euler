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

    for n in range(50, 5000):
        f = fib(n)
        if len(str(f)) == 1000:
            print n
            break
