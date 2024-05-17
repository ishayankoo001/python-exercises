import tree

def ex1(tree1, tree2):
    t3 = tree.BinaryTree(subtree_sum(tree1) + subtree_sum(tree2))
    if tree1.left:
      t3.left = ex1(tree1.left, tree2.left)
    if tree2.right:
      t3.right = ex1(tree1.right, tree2.right)
    return t3

def subtree_sum(subtree):
    sum = subtree.value
    if subtree.left:
      sum += subtree_sum(subtree.left)
    if subtree.right:
      sum += subtree_sum(subtree.right)
    return sum