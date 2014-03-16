#!/usr/bin/python

end = (2, 2)
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
            self.right = Tree((pos_x + 1, pos_y))
            self.down = Tree((pos_x, pos_y + 1))
        self.pos = pos

if __name__ == "__main__":

    t = Tree((0,0))
    print tally
