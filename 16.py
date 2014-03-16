#!/usr/bin/python

if __name__ == "__main__":

    sum = 0

    for c in str(2 ** 1000):
        sum += int(c)

    print sum
