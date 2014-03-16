#!/usr/bin/python

start = (0, 0)
end = (6, 6)
tally = 0

class Tree(object):
    def __init__(self, pos):
        global tally
        (pos_x, pos_y) = pos
        (end_x, end_y) = end
        if (pos_x, pos_y) == end:
            self.right = end
            self.down = end
            tally += 1
        elif pos_x == end_x:
            self.down = Tree((pos_x, pos_y + 1))
            self.right = True
        elif pos_y == end_y:
            self.right = Tree((pos_x + 1, pos_y))
            self.down = True
        else:
            if pos == start:
                self.right = Tree((pos_x + 1, pos_y))
            else:
                self.right = Tree((pos_x + 1, pos_y))
                self.down = Tree((pos_x, pos_y + 1))
        self.pos = pos

if __name__ == "__main__":

    t = Tree(start)
    print tally * 2
