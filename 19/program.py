def es19(ftext):
    '''A 2-dimensional matrix of integers is registered within a text
    file.  The file contains empty lines interspersed with lines
    corresponding to the rows of the matrix.

    Inside the lines corresponding to the matrix rows, each integer of
    the matrix row appears preceded by one or more spaces.  See for
    example the file fm10_1.txt where the following matrix is
    registered:
     1 20  3 40  5
    60  7  8  9 10
    11 12 13 14 15
    Deisgn and implement a function es19(ftext) that,
    - takes as argument the path to a text file in which the matrix of
      integer is written
    - returns a pair (tuple) containing:
        - the matrix as a list of list of integer 
        - the sum of the elements of the outer frame of the matrix,
          namely, the first and the last rows and the first and last
          columns of the matrix.
    For example for filefm10_1.txt the function must return:
        ([[ 1, 20,  3, 40,  5],
          [60,  7,  8,  9, 10],
          [11, 12, 13, 14, 15]],
          204)
    '''
    pass
