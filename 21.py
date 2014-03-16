#!/usr/bin/python

sumstore = {}

def get_divisors(n):

    d = []

    for x in range(1, int(n*0.5)+1):
        if n % x == 0:
            d.append(x)

    return d

if __name__ == "__main__":

    tally = 0

    for i in range(2, 10001):
        d = get_divisors(i)
        sumstore[i] = sum(d)

    for num in sumstore.keys():
        if num in sumstore.values() and sumstore[num] in sumstore and sumstore[sumstore[num]] == num and num != sumstore[num]:
            tally += num

    print tally
