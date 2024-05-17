import treenode

def es7(tree, id_set,k):
    '''Design and implement the recursive function es7(tree, id_set, k) (or that uses
        recursive function(s) or method(s)) that:
        - takes as arguments:
          - a tree 'tree' formed by nodes of the type Node defined in
            the library treenode.py,
          - a set 'id_set' of integers
          - an integer 'k'
        - returns the number of tree nodes having
          EXACTLY k children who have identifiers in the id_set.

        Example: let k=2 and id_set={1,2,3,5,9}, so function es7
        - returns 2 on the left tree (for children of nodes 4 and 2)
        - returns 3 for the right tree (for the children of nodes 7, 9 and 10).

                  5                                     7
          ________|_____________                _______|______
         |          |           |              |              |
         20         4           6              5              9
         |     _____|______                 ___|___        ___|__
         11   |   |  |  |  |               |       |      |      |
              10  2  9  8  7               10      8      3      1
                __|__                     _|_     _|_    _|_    _|_
               |     |                   |   |   |   |  |   |  |   |
               3     1                   1   2   12  13 15  6  4   0

    '''


    sum = 0
    l = 0
    for son in tree.sons:
        if son.id in id_set:
            l += 1
    if l == k:
        sum += 1
    for son in tree.sons:
        sum += es7(son, id_set, k)  # accumulate count from recursive call
    return sum  # return the accumulated count




