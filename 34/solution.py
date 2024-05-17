import json


def ex34(fname1, fname2):
    square = []
    with open(fname1, encoding='utf8') as f:
        square = json.load(f)
    symbols = set(square[0]).union(set(square[1]))
    N = len(symbols)
    for line in square:
        line.append((symbols-set(line)).pop())
    last = []
    for c in range(N):
        col = set(l[c] for l in square)
        last.append((symbols-col).pop())
    square.append(last)
    with open(fname2, mode='w', encoding='utf8') as f:
        json.dump(square, f)
    return symbols
