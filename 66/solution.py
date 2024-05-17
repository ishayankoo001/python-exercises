import tree


def ex66(tree):
    m, M = max_treewidth(tree)
    return M-m


def max_treewidth(A, pos=0):
    sx_m = sx_M = dx_m = dx_M = pos         # if a leaf, minpos=maxpos
    if A.sx:
        sx_m, sx_M = max_treewidth(A.sx, pos-1)
    if A.dx:
        dx_m, dx_M = max_treewidth(A.dx, pos+1)
    return min(sx_m, dx_m), max(sx_M, dx_M)
