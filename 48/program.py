import tree
from tree import BinaryTree


def ex48(tree):
    if tree == None:
        return 0
    count = 0
    if tree.sx != None and tree.dx != None:
        count += 1
    count += ex48(tree.sx) + ex48(tree.dx)
    return count



    '''
             7
            /\
           1  3
          / \
        4    6
       /    /
      5    2
     /     \
    9       8

    the function will return the value 2, since there are only two
    nodes with exactly two children, namely the nodes with value 7 and
    1.

    '''
    # insert here your code

