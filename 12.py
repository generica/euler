#!/usr/bin/python

trianglestore = {}

def get_divisors(n):

    d = []

    for x in range(1, int(n*0.5)+1):
        if n % x == 0:
            d.append(x)

    d.append(n)

    return d

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
        d = get_divisors(t)
        n = len(d)

        if n > 500:
            print t, d, n
