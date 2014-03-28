#!/usr/bin/python

def check_same_digits(num1, num2):

    l1 = [c for c in str(num1)]
    l2 = [c for c in str(num2)]

    l1.sort()
    l2.sort()

    if l1 == l2:
        return True
    else:
        return False


if __name__ == "__main__":

    for i in xrange(1, 1000000000000):
        if check_same_digits(i, 2 * i):
            if check_same_digits(i, 3 * i):
                if check_same_digits(i, 4 * i):
                    if check_same_digits(i, 5 * i):
                        if check_same_digits(i, 6 * i):
                            print "%s" % (i)
                            break
