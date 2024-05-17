import tree

def prepare(tree):
    root = tree.value
    if tree.dx != None:
        tree.dx.value = root + 1
        ex66(tree.dx)
    if tree.sx != None:
        tree.sx.value = root - 1
        ex66(tree.sx)

def ex66(tree):
    prepare(tree)
    values = []
    if(tree.sx == None and tree.dx == None):
        return values
    if(tree.dx != None):
        values.append(tree.value)
        ex66(tree.dx)
    if(tree.sx != None):
        values.append(tree.value)
        ex66(tree.dx)







    """Design  a function ex66(tree) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as argument a tree that consists of nodes of type
      BinaryTree, defined in the attached tree.py library,
    - it returns the "maximum width" of the tree, i.e. the
      difference between the position of the rightmost node of the
      tree and the position of the leftmost node of the tree

    The position of a node with respect to the root (which we assume
    is at position 0) can be computed following the path from the root
    to such a node: subtract 1 (one) whenever following a left
    subtree, add 1 (one), whenever following a right subtree.
    Example: if the tree is the one below on the left, the positions
    will be those in the tree on the right:

             1           .            0         .
            / \          .           / \        .
           2   3         .         -1   1       .
          / \            .        /  \          .
        4    5           .      -2    0         .
       /    /            .      /    /          .
      6    7             .    -3    -1          .
       \    \            .      \    \          .
        8    9           .      -2    0         .

    The leftmost node (with value 6) is at position -3.
    The rightmost node (with value 3) is at position 1.
    Then the function returns the value 4=1-(-3).

    """
    # insert here your code
t = tree.BinaryTree.fromList([0, [-5, None, None],[1, [0, None, None],[2, None, None],],])
print(ex66(t))
