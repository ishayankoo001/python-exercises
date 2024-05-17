
def es77(word):
    suffixes = []
    for i in range(len(word)-1, -1, -1):
        suffixes += [word[i:]]
    return suffixes
