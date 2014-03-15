#!/usr/bin/python

if __name__ == "__main__":

    sumsquares, squaresums = 0, 0

    for x in range(1, 101):
        sumsquares += x ** 2
        squaresums += x

    print (squaresums ** 2) - sumsquares
