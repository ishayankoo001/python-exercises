

def ex60(textfile, textfile2):
    '''Design and implement the function ex60(textfile, textfile2) such that:
    - it receives as arguments two filenames ('textfile' and
      'textfile2') of text files
    - it reads the content of 'textfile', that consists of the rows of
      a matrix made of integers between 1 and 9, separated by whitespaces
    - it modifies the matrix and writes the resulting matrix in 'textfile2'
    - it returns the number of columns of the matrix that were modified.
    The matrix is modified so that all the values of odd columns are
    replaced with a zero.  A column in the matrix is called "odd" if
    most of its elements are odd (that is, if the number of odd
    elements is equal or lower than the number of even elements, the
    row is not odd).

    Example: if the file in textfile contains the following rows
    1 2 3 4 5 7
    3 4 4 4 4 5
    3 1 4 6 3 1
    2 5 8 1 7 3
    the function will return the value 3 and textfile2 will contain
    the following rows
    0 2 3 4 0 0
    0 4 4 4 0 0
    0 1 4 6 0 0
    0 5 8 1 0 0

    '''
    # insert here your code
