def ex60(textfile, textfile2):
    matrix = []
    with open(textfile) as fIn:
        for line in fIn:
            values = list(map(int, line.split()))
            matrix.append(values)
    w = len(matrix[0])
    h = len(matrix)
    numodd = 0
    for c in range(w):
        countodd = 0
        for r in range(h):
            countodd += matrix[r][c] % 2
        if countodd > h-countodd:
            numodd += 1
            for r in range(h):
                matrix[r][c] = 0
    with open(textfile2, mode='w') as fOut:
        fOut.write('\n'.join(' '.join(map(str, row)) for row in matrix))
    return numodd
