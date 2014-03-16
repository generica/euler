#!/usr/bin/python

start = (0,0)
end = (2,2)

def next_moves(pos):

   (pos_x, pos_y) = pos
   if (pos_x + 1, pos_y) == end or (pos_x, pos_y + 1) == end:
       return (True, end)
   else:
       return ((pos_x + 1, pos_y), (pos_x, pos_y + 1))

if __name__ == "__main__":

    pos = start
    moves = []

    while True:
        (next_1, next_2) = next_moves(pos)
        print next_moves(next_1), next_moves(next_2)
