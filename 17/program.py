

def es17(ls, k):
    '''Design  function es17(ls,k) that receives as input
    - a list ls of words
    - an integer k

    and deletes from ls all the words that contain at least k equal
    characters. No distinction has to be made between uppercase and
    lowercase. The function also returns the number of deleted words.
    
    For example,
    - if ls=[ 'ananas', 'pera', 'banana', 'melone', 'kiwi','albicocca']
    - and k=3
    the function returns 3 and the list becomes ['pera', 'melone', 'kiwi']

    - if ls=[ 'Angelo', 'Andrea', 'Osvaldo', 'Anna', 'Monica', 'Adele'] and k=2
    the function returns 4 and the list becomes ['Angelo', 'Monica']

    '''
    newls = []
    for word in ls:
        if(shouldAdd(buildDictionary(word.lower()),k)):
            newls.append(word)
    num = len(ls) - len(newls)
    ls[:] = newls[:]
    print(ls)
    return num


def buildDictionary(word):
    mydict = {}
    for letter in word:
        if letter in mydict:
            mydict[letter] += 1
        else:
            mydict[letter] = 1
    print(mydict)
    return mydict
def shouldAdd(dictionary: dict, k):
    for item in dictionary.items():
        print(item)
        if item[1] >= k:
            return False
    return True
print(es17(['Angelo', 'Andrea', 'Osvaldo', 'Anna',
          'Monica', 'Adele'],2))


