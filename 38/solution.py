import copy


def es38(maze):
    # I can't modify the maze, so I create a copy of it
    # I copy the labyrinth so I can edit it
    lab = [[v for v in row] for row in maze]

    # to understand if a cell is reachable just look at the two above and to the left)
    # I use the value 2 to indicate that the cell is reachable
    # I mark the first box as reachable
    lab[0][0] = 2
    # and remember initial position
    pos = (0, 0)
    # I scan the matrix first by rows and then by columns
    # so that the last reachable cell found is also the lower right cell
    # I scan the matrix from top to bottom
    for y, row in enumerate(lab):
        for x, cell in enumerate(row):              # and from left to right
            # if the current box is empty
            # and to the right of a reachable one or under a reachable one
            if cell == 0 and ((y > 0 and lab[y-1][x] == 2) or (x > 0 and lab[y][x-1] == 2)):
                # I mark it as reachable
                lab[y][x] = 2
                pos = x, y                          # make a note of it
    return pos                                      # and at the end I return it
