#!/usr/bin/python

def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

import itertools

if __name__ == "__main__":

    list = []
    largest = 0

    for i in range(1, 10):
        list.append(i)
        for num in itertools.permutations(list):
            s = ""
            for i in num:
                s = "%s%d" % (s, i)
            if isprime(int(s)): 
                if int(s) > largest:
                    largest = int(s)

    print largest
