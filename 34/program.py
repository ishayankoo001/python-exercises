import json


def ex34(fname1, fname2):
    '''A Latin square is an n × n array filled with n different symbols,
    each occurring exactly once in each row and exactly once in each
    column.

    Design a function ex34(fname1,fname2) such that:
    - it takes as argument two filenames ('fname1' and
      'fname2'). 'fname1' is a json file in which is stored a Latin
      square, where the last row and the last column are missing. The
      Latin square is represented as a list of lists
    - it saves in 'fname2' the Latin square completed with the missing
      column and row. The Latin square is saved as a list of lists in
      json format
    - it returns a set containing all the symbols that appear in the
      completed Latin square.

    Example: if the partial Latin square in fname1 is represented as
    the list of lists [['X','1'],['?','X']], then,
    the set with the symbols of the Latin square will be {'X','1','?'}
    and the complete Latin square will be saved in fname2 as
    [['X','1','?'],['?','X','1'],['1','?','X']]

    Note: assume that it is always n>2

    '''
    # insert here your code
