def es36(dictionariesList: list[dict]):
    '''Implement the function es36(dictionariesList) that takes as an
    input a list of dictionaries and returns a dictionary.

    The input dictionaries in the dictionariesList have character
    strings between 'a' and 'z' as key and lists of integers as
    attributes.

    The keys in the output dictionary are the keys common to all the
    dictionaries in dictionariesList.  Each x key of the output
    dictionary is associated with a list of integers.  An integer is
    present in the list of a key x if and only if it is present in the
    attribute list of key x for all the dictionaries of
    dictionariesList.  The list is also sorted in ascending order.

    For example:
    - if the dictionariesList contains the three dictionaries
    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    - the returned dictionary is
    {'a':[3,5],'d':[]}

    '''
    keys = []
    d = {}
    for dict in dictionariesList:
        keys.extend(dict.keys())
    keys = list(set([x for x in keys if find_occurences(keys,x)==len(dict)]))
    d = {k:[] for k in keys}
    for dict in dictionariesList:
        for k in keys:
            d[k].extend(dict[k])
    for a,v in d.items():
       d[a] = list(set([x for x in d[a] if find_occurences(d[a],x)==len(dict)]))


    return(d)


def find_occurences(l, w):
    s = 0
    for i in l:
        if i == w:
            s += 1
    return s
l = [    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}]
es36(l)