

def es57(grid):
    '''The skyscrapers puzzle places skyscrapers in a square grid NxN so
      that each row and column contains only skyscrapers of different
      heights (integer values from 1 to N).  The game is to find the
      positions of all the skyscrapers. At the beginning, it is given
      the number of skyscrapers visible for each row and column along
      the 4 sides of the grid, considering that a skyscraper of height
      h hides any skyscraper with a lower height. Then, four lists are
      given (North, East, South and West) each of length N such that
      for 0<i<N:
 
       - North[i] contains the number of skyscrapers visible in column
         i of the grid when looking from the north.
      
       - East[i] contains the number of skyscrapers visible in row i
         of the grid when looking from the east.

       - South[i] contains the number of skyscrapers visible in column
         i of the grid looking from the south.
  
       - West[i] contains the number of skyscrapers visible in row i
         of the grid looking from west.

    Write the function es57(grid) that, given 
    
    - a square grid NxN, represented by list of lists of integers in which
      each list is a line of the matrix,

    must return:

    - a tuple in which the 4 lists North, East, South and West appear
      in such an order, if the grid is a valid skyscraper puzzle;

    - a tuple of four empty list, otherwise (i.e.: the grid is not a
    valid skyscrapers puzzle). This can happen because there are
    repeated numbers in a row or column, or because there are numbers
    outside the range 1-N or because there are non numerical values.

    For example
    - if grid = [[1,2,3,4],[4,1,2,3],[3,4,1,2],[2,3,4,1]] the function
      returns ([2,2,2,1],[1,2,2,2],[3,2,1,4],[4,1,2,3]).

    - if grid = [[1,2,3,4],[4,1,c',3],[3,4,1,2],[2,3,4,1]] or
         grid = [[1,2,3,4],[4,1,2,3],[3,4,2,1],[2,3,4,1]] or
         grid = [[1,2,3,4],[4,1,2,3],[3,4,1,2],[2,3,6,1]] the function
      returns ([],[],[],[]).

    '''
    #Enter your code here
