import treenode
def pack_in_two(ls):
    newlist=[]
    for i in range(0,len(ls)-1,2):
        newlist.append([ls[i], ls[i+1]])
    return newlist
def fooler(a):
    if a == 1:
        return 0
    fooler(a-1)
def nodize(list):
    newls = []
    for i in list:
        left = treenode.Node(i[0])
        right = treenode.Node(i[1])
        newls.append([left,right])
    return newls
def createTree(list):
    newls = []
    if len(list)==1:
        v = list[0][0].id + list[0][1].id
        father = treenode.Node(v)
        father.sons = list[0]
        return father
    for node in list:
        v = node[0].id + node[1].id
        father = treenode.Node(v)
        father.sons = node
        newls.append(father)
    print(newls)
    newls = pack_in_two(newls)
    print(newls)
    return createTree(newls)

def es12(k):
    fooler(3)
    list = [i for i in range(1,2**k+1)]
    list = pack_in_two(list)
    list = nodize(list)
    a=(createTree(list))

    print(a)
    print(treenode.toLista(a))
    return a



    """A tree is said complete binary if all its internal nodes have
        exactly 2 children and all the leaves are on the same level.
        Design and implement the recursive function es12(k) (or function
        that uses recursive function(s) or recursive method(s)) that:
        - takes as argument an integer k
        and constructs a complete binary tree with height k consisting of
        nodes of type Node, as defined in the library treenode.py. Leaf
        identifiers, read from left to right are the 2^k-integers ranging
        from 1 to 2^k (note that a complete binary tree with height k
        always has 2^k leaves). The identifiers of the internal nodes are
        given by the sum of the identifiers of their two children.
        The function returns as a result the root of the built tree.
        Example:
        - es12(2) creates and returns the tree on the left
        - es12(3) creates and returns the tree on the right
    
                        10                                  36
                 _______|______                      _______|______
                |              |                    |              |
                3              7                   10             26
             ___|___        ___|__               ___|___        ___|__
            |       |      |      |             |       |      |      |
            1       2      3      4             3       7     11     15
                                               _|_     _|_    _|_    _|_
                                              |   |   |   |  |   |  |   |
                                              1   2   3   4  5   6  7   8
    
    """
es12(3)


