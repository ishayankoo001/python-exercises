def es21(matrix):
    '''Design function es21(matrix) that takes as input a matrix of
     characters represented by a list of character lists and returns a
     new matrix where the columns of the input matrix are
     alphabetically ordered. At the end of the function, the input
     matrix should not be modified.

     For example, if the input matrix is
     [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']] 

    the function will return the matrix:
     [['a','a','g','f'],
      ['b','b','m','g'],
      ['q','s','n','z']]

    '''
    cols = []
    newmatrix = []
    for i in range(len(matrix[0])):
        for j in matrix:
            cols.append(j[i])
    cols = [sorted(cols[x:x+len(matrix)]) for x in range(0,len(cols),len(matrix))]
    for i in range(len(cols[0])):
        for j in cols:
            newmatrix.append(j[i])
    print(newmatrix)
    newmatrix = [newmatrix[x:x+len(matrix[0])] for x in range(0,len(newmatrix), len(matrix[0]))]

    return newmatrix

