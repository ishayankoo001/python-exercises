

def es40(jsonFile,k):
    '''Given a matrix of integers M, we can say that its coordinate (x,y)
    identifies a square of side k if in the 4 positions M[y][x],
    M[y][x+k], M[y+k][x+k] and M[y+k][x] we find in order an
    increasing sequence of 4 integers.

    For example in the matrix
      2  3  3  6  1
      2  8  5  1  9 
      5  4 40  4  5
      9 10  1  7  6
     12 11  9  8 10
     - the coordinate (1,1) identifies a square of side 3 (whose
       sequence is 8,9,10,11)
     - the coordinate (3,2) identifies a square of side 1 (whose
       sequence is 4,5,6,7)
     - the coordinate (0,3) identifies a square of side 1 (whose
       sequence is  9,10,11,12)
 
    Design and implement the function es40(jsonFile, k), that takes as
    arguments:
    - jsonFile: the path of a json file containing a matrix
    represented as a list of lists of integers
    - an integer k
    and searches inside the matrix in the json file for the possible
    presence of a square of side k.
    The function returns the tuple representing one coordinate (x,y)
    that locates the square of side k.
    If the matrix contains more squares of side k, the function
    returns the coordinate that identifies the one at the bottom right
    (i.e. the one for which the row is maximum and the column is
    equal).
    If the matrix does not contain squares of side k, it returns
    the tuple (-1,-1).

    For the example matrix and k = 2 the function returns (-1,-1).
    For the example matrix and k = 1 the function returns (0, 3).

    '''
    # insert here your code











