def es53(ftext):
    with open(ftext, encoding='utf8') as f:
        text = f.read()
    lst = text.split(':')
    for i in range(len(lst)):
        lst[i] = [int(x) for x in lst[i].split()]
    lst1 = [[lst[i-1][-1]]+lst[i][:-1] for i in range(1, len(lst)-1)]
    lst1 += [[lst[-2][-1]]+lst[-1]]
    return {elem[0]: elem[1:] for elem in lst1}
