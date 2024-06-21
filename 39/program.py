import json


def ex39(n, jsonFile):
    '''Given an integer n, a spiral matrix of order n is a matrix of
    dimensions n x n which shows the numbers from 1 to n**2, following
    a clockwise spiral.  For example the spiral matrix of order 4 is
    
     1 2 3 4 
    12 13 14 5
    11 16 15 6
    10 9 8 7 
    
    Design a function ex39(n, jsonFile) such that
    - it takes as argument an int 'n' and the path of a json file 'jsonFile'
    - it writes in json format in the file 'jsonFile' the list of
      lists representing the spiral matrix of order n
    - it returns the sum of the values in the columns with the even
      indexes of the matrix.

    Example: for n=4 the jsonFile will contain
     [[1, 2, 3, 4],[12, 13, 14, 5],[11, 16, 15, 6], [10, 9, 8, 7]]
     and the value returned will be 74.

    '''
    mat = [[0 for i in range(n)] for i in range(n)]
    left = 0
    right = n - 1
    top = 0
    bottom = n - 1
    count = 1
    while(left<=right and top<=bottom):
        for i in range(left, right + 1):
            mat[top][i] = count
            count += 1
        top += 1
        for i in range(top, bottom+1):
            mat[i][right] = count
            count += 1
        right -= 1
        for i in range(right, left-1, -1):
            mat[bottom][i] = count
            count += 1
        bottom -= 1
        for i in range(bottom, top -1,-1):
            mat[i][left] = count
            count+=1
        left+=1
    sums = 0
    temp = list(zip(*mat))
    for i in range(0,len(mat),2):
        sums += sum(temp[i])

    with open(jsonFile,"w") as f:
        json.dump(mat,f)


    return sums
print(ex39(4,"a.json"))

