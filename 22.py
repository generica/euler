#!/usr/bin/python

def get_name_score(name):

    tally = 0

    for char in name.lower():
        if char != '"':
            tally += (ord(char) - 96)

    return tally

if __name__ == "__main__":

    i = 1
    tally = 0

    names = open('names.txt', 'r').read().strip().split(",")
    for name in sorted(names):
        tally += (i * get_name_score(name))
        i += 1

    print tally
