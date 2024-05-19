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
    newmat = list((zip(*matrix)))
    print(newmat)
    newnewmat = []
    for i in newmat:
        newnewmat .append(list(sorted(i, key=lambda x:x)))
    newnewmat = list(zip(*newnewmat))
    newnewmat = [[*x] for x in newnewmat]


    return newnewmat
matrix = [['q','s','g','g'],
      ['b','a','m','f'],
      ['a','b','n','z']]
print(es21(matrix))

