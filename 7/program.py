import treenode


def es7(tree, id_set, k):
    if tree is None:
        return 0
    count = sum(1 for child in tree.sons if child.id in id_set)
    suma = 1 if count==k else 0
    for l in tree.sons:
        suma += es7(l,id_set,k)
    return suma
