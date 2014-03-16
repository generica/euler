#!/usr/bin/python

def count(num):

    if num == 0:
        return 0
    elif num == 1 or num == 2 or num == 6 or num == 10:
        return 3
    elif num == 4 or num == 5 or num == 9:
        return 4
    elif num == 3 or num == 7 or num == 8 or num == 40 or num == 50 or num == 60:
        return 5
    elif num == 11 or num == 12 or num == 20 or num == 30 or num == 80 or num == 90:
        return 6
    elif num == 15 or num == 16 or num == 70:
        return 7
    elif num == 13 or num == 14 or num == 18 or num == 19:
        return 8
    elif num == 17:
        return 9
    elif num == 20:
        return 6
    elif num < 100:
        base = str(num)[0]
        end = str(num)[1]
        return count(int("%s0" % (base))) + count(int(end))
    elif num < 1000:
        base = str(num)[0]
        end = str(num)[1:]
        if num % 100 == 0:
            return count(int(base)) + 7
        else:
            return count(int(base)) + 10 + count(int(end))
    elif num == 1000:
        return 11

if __name__ == "__main__":

    sum = 0

    for i in range(1, 1001):
        sum += count(i)

    print sum
