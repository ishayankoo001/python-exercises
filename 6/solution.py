import tree

def ex6(paths):
    lstPaths = list(paths)
    root = tree.BinaryTree(lstPaths[0][-1:])
    for a_path in lstPaths:
        root = constructPath(root, a_path[:-1])
    return root



def constructPath(root, pathStr):
    if(pathStr == ''):
        return root
    lastChar = pathStr[-1:]
    if(lastChar > root.value):
        if(root.dx == None):
            root.dx = tree.BinaryTree(lastChar)
            constructPath(root.dx, pathStr[:-1])
        else:
            constructPath(root.dx, pathStr[:-1])
    elif(lastChar < root.value):
        if(root.sx == None):
            root.sx = tree.BinaryTree(lastChar)
            constructPath(root.sx, pathStr[:-1])
        else:
            constructPath(root.sx, pathStr[:-1])
    return root
