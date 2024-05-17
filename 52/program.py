# A matrix is said to be sparse if it has few values other than
# zero. To save space of memory, instead of using lists of lists we
# can use sparse matrices by means of dictionaries. The dictionary of
# a sparse matrix M has tuples as keys and an integer as an
# attribute. Tuples are pairs and the pair (i,j) is present in the
# dictionary if and only if M[i][j] is different from zero. The
# attribute of the key (i,j) will be then just M[i][j].

# EXAMPLE
# the dictionary d={(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 }
# represents the square matrix
#    | 0 0 4 | 
# M= | 1 2 0 |
#    | 0 8 0 |

def es52(d1,d2):
    '''Define the function es52(d1,d2) that receives as input

    - two dictionaries of sparse matrices of the same size

    and returns a dictionary with the sparse matrix sum of the two
    input matrices.

    For example if
      d1={(0.2): 4,(1.0): 1, (1.1): 2, (2.1):8 } and
      d2={(0.0): 5,(1.1): 2, (2.2): 5, (1.0):2 }.

    then the function has to return the dictionary 
      {(0,2): 4,(1,0): 3, (1,1): 4, (2,1):8, (0,0):5, (2,2):5 }

    NOTICE: Input dictionaries must NOT be modified

    '''
    # enter your code here

