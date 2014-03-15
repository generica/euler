#!/usr/bin/python

def next_num(num):

    if num % 2 == 0:
        return num / 2
    else:
        return (3 * num) + 1

def generate(start):

    seq = []
    n = start

    while True:
        seq.append(n)
        p = next_num(n)
        if p == 1:
            seq.append(p)
            return seq
        n = p


if __name__ == "__main__":

    best = 0
    best_start = 0

    for i in range(2, 1000001):
        n = generate(i)
        if len(n) > best:
            best = len(n)
            best_start = i

    print best_start, best
