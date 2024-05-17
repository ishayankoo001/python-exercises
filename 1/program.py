import tree


def ex1(tree1, tree2):
    '''
    Ex 1: 6 points.
    Design and implement a function ex1(tree1, tree2) such that:
    - it is recursive or uses recursive functions(s)/method(s);
    - it receives two trees as arguments ('tree1' and 'tree2') that consist of
      nodes of type BinaryTree, defined in the attached tree.py library;
    - it generates a tree of type BinaryTree;
    - it returns the generated tree’s root as a result.
    The two input trees have the same structure but the information contained in
    the value attribute of the corresponding nodes may be different. The tree to
    be generated should have the same structure of the two input trees. The
    value of the nodes of the new tree is computed according to the following
    rule.
    Let z be a node in the generated tree, x and y be the two corresponding
    nodes of tree1 and tree2, respectively. To compute the value of z, operate
    as follows:
    - Compute the sum of the values of the nodes in the subtree of tree1 rooted
      in x;
    - Compute the sum of the values of the nodes in the subtree of tree2 rooted
      in y;
    - The sum of the two sums above is assigned to the value of z.
    Example: if tree1 and tree2 are the two trees below on the left-hand side,
    then the returned tree will be the one below on the right-hand side.

    WARNING: - The use of the functions of the BinaryTree class is FORBIDDEN.
             - The two input trees should not be changed.

             1              7            90           |
            /\             /\            /\           |
           2  3           1  3         76  6          |
          / \            / \           / \            |
        4    5          4   6        36  37           |
       /    /          /   /         /   /            |
      6    7          5   2         28 26             |
     /     \         /    \        /    \             |
     8      9       9      8      17    17            |
    '''
    t = tree.BinaryTree(calculateSum(tree1) + calculateSum(tree2))
    if tree1.right:
        t.right=ex1(tree1.right,tree2.right)
    if tree1.left:
        t.left = ex1(tree1.left, tree2.left)
    return t



def calculateSum(tree):
    sum = 0
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return tree.value
    if tree.right != None:
        sum += calculateSum(tree.right)
    if tree.left != None:
        sum += calculateSum(tree.left)
    sum += tree.value
    return sum
list1 = [9,[2,[6,[5, None, None],[5, None, None]],[6,[5, None, None],[5, None, None]]],
         [4,[6,[5, None, None],[5, None, None]],[6,[5, None, None],[5, None, None]]]]
list2 = [4, [4, [5, [1, None, None], [6, None, None]], [6, [6, None, None], [1, None, None]]],
         [4, [7, [1, None, None], [6, None, None]], [8, [6, None, None], [1, None, None]]]]
list3 = [145, [63, [28, [6, None, None], [11, None, None]], [29, [11, None, None], [6, None, None]]],
         [69, [30, [6, None, None], [11, None, None]], [31, [11, None, None], [6, None, None]]]]
tree1 = tree.BinaryTree.fromList(list1)
tree2 = tree.BinaryTree.fromList(list2)
print(ex1(tree1,tree2))




