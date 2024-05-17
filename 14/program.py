
import bintree
def es14(tree, x):
  '''Design and implement a recursive function es14(tree,x) (or a
      function that makes use of recursive function(s) or methods(s))
      that takes as arguments:
      - 'tree', a binary tree formed by nodes of type BinTree defined
          in the  library bintree.py
      - an integer 'x'
      and calculates the number of nodes in the tree that have value
      divisible by x+level, where level is the level of the node. The
      function returns as a result the calculated number.
      WARNING:  it is FORBIDDEN to use methods of the library bintree

      Example: if x = 2 and the tree is:

              7
              /\
            1  3
            / \
          4    6
        /    /
        5    2
      /     \
      9       8
      
      the function returns the value 3, since in the tree there are 3
      nodes with value divisible by 2+level, namely the nodes with
      value 3,4 and 5.

  '''
  sum = 0
  if(tree == None):
    return sum
  if tree.value % x == 0:
    sum += 1

  sum += es14(tree.sx, x+1) + es14(tree.dx, x+1)
  return sum




