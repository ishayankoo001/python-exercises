

def es61(ftext, op, sel):
    matrix = []
    with open(ftext) as fIn:
        for line in fIn:
            matrix.append(list(map(int, line.split())))
    l = len(matrix)
    resM = []
    resm = []
    ress = []
    if sel == 'row':
        for row in matrix:
            M = m = row[0]
            s = 0
            for v in row:
                M = max(M, v)
                m = min(m, v)
                s += v
            resM.append(M)
            resm.append(m)
            ress.append(s)
    elif sel == 'col':
        for c in range(l):
            M = m = matrix[0][c]
            s = 0
            for r in range(l):
                v = matrix[r][c]
                M = max(M, v)
                m = min(m, v)
                s += v
            resM.append(M)
            resm.append(m)
            ress.append(s)
    elif sel == 'dp':
        M = m = matrix[0][0]
        s = 0
        for c in range(l):
            v = matrix[c][c]
            M = max(M, v)
            m = min(m, v)
            s += v
        resM.append(M)
        resm.append(m)
        ress.append(s)
    else:
        M = m = matrix[0][l-1]
        s = 0
        for c in range(l):
            v = matrix[c][l-1-c]
            M = max(M, v)
            m = min(m, v)
            s += v
        resM.append(M)
        resm.append(m)
        ress.append(s)
    if op == 'max':
        return resM
    elif op == 'min':
        return resm
    else:
        return ress
