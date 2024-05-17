def es45(word1, word2):
    sub1 = set()
    sub2 = set()
    l1 = len(word1)
    for i in range(l1):
        for j in range(i, l1):
            sub1.add(word1[i:j+1])
    l2 = len(word2)
    for i in range(l2):
        for j in range(i, l2):
            sub2.add(word2[i:j+1])
    return sorted(sub1.intersection(sub2))