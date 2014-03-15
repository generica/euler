#!/usr/bin/python

import math

trianglestore = {}

def get_num_divisors(n):

    tally = 0

    for x in range(1, int(math.sqrt(n))+1):
        if n % x == 0:
            tally += 1

    return 2 * tally

def generate_triangle(num):

    if num == 0:
        return 0

    if num == 1:
        triangle = 1

    if (num - 1) in trianglestore:
        triangle = trianglestore[num -1] + num
    else:
        triangle = generate_triangle(num - 1) + num

    trianglestore[num] = triangle
    return triangle

if __name__ == "__main__":

    for i in xrange(1, 1000000000000):
        t = generate_triangle(i)
        n = get_num_divisors(t)

        if n > 500:
            print t, n
            break
