
def es77(word):
    '''
    Define a NOT recursive function, NOT using any recursive functions, es77(word),
    which takes a string of characters as input. The function returns the list of
    all the suffixes of the string.
    The elements of the list must be sorted by increasing length.

    Remember that a suffix of a word is what you get by deleting 0 or more 
    initial characters from the word.
    Example: es77("fondamenti") should return
    ['i', 'ti', 'ti', 'nti', 'enti', 'enti', 'menti', 'amenti', 'damenti', 'ndamenti', 'ondamenti', 'fondamenti']
    '''
    s = ""
    ls = []
    for i in range(len(word)-1,-1,-1):
        s= word[i]+s
        ls.append(s)
    return ls
print(es77(("fondamenti")))

