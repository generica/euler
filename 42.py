#!/usr/bin/python

triangles = []

def gen_triangles():
    global triangles

    for i in range(1, 1000):
        triangles.append(i * (i + 1) / 2)

def is_triangle(word):

    tally = 0

    for char in word.lower():
        if char != '"':
            tally += (ord(char) - 96)

    if tally in triangles:
        return 1
    else:
        return 0

if __name__ == "__main__":

    tally = 0

    gen_triangles()

    words = open('words.txt', 'r').read().strip().split(",")
    for word in words:
        tally += is_triangle(word)

    print tally
