import os
import os.path


def es67(path):
    minimum = {}
    maximum = {}
    minmax(path, minimum, maximum, 0)
    return {k: maximum[k]-minimum[k] for k in minimum}


def minmax(path, m, M, prof):
    for fn in os.listdir(path):
        if '.' == fn[0]: continue
        filename = path + '/' + fn
        if os.path.isdir(filename):
            minmax(filename, m, M, prof+1)
        else:
            ext = fn[-3:]
            m[ext] = min(m.get(ext, prof), prof)
            M[ext] = max(M.get(ext, prof), prof)
