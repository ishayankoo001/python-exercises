
import copy

def es38(labyrinth):
    '''A labyrinth is represented by a grid (list of lists).  Labyrinth
    cell positions are determined by pairs (x,y) where y is the row
    and x is the column in which the cell is located.
    The cell at the top left has coordinates (0,0).
    The grid cells contain the integer 0 (free) or the integer 1
    (obstacle).
    You can move between two adjacent cells only if the destination
    cell contains the integer 0 (it is empty) AND with only two types
    of moves:
    - from top to bottom (from a generic cell (x,y) to the cell
    (x,y+1) )
    - from left to right (from a generic cell (x,y) to the cell
    (x+1,y) )

    A cell (x,y) is reachable if there is at least a sequence of moves
    that starts from the cell (0,0) and terminates in (x,y).

    Write the function es38(labyrinth) which takes as an input a
    labyrinth represented as above and returns the coordinates (x, y)
    of the lowest reachable cell and (in case of tie) the rightmost
    one.

    For example: for the 7x7 size labyrinth:
    0001000
    1000010
    0001010
    1010010
    0011010
    1001011
    0110100

    the function must return the tuple (4, 5).

    Note: The list of lists must not be changed by the function.

    '''
    # insert here your code
