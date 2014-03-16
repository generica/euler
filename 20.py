#!/usr/bin/python

facts = {}

def compute_fact(n):
    if n == 1:
        facts[n] = 1
        return 1
    if n - 1 in facts:
        f = facts[n - 1] * n
        facts[n] = f
        return f
    f = compute_fact(n - 1) * n
    facts[n] = f
    return f

if __name__ == "__main__":

    sum = 0

    f = compute_fact(100)
    for c in str(f):
        sum += int(c)

    print sum
