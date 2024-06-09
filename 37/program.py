

def es37(dictionariesList: [dict]):
    '''Write the function es37(dictionariesList) that takes as an input a
    list of dictionaries and returns a dictionary.

    The input dictionaries in dictionariesList have character strings
    between 'a' and 'z' as keys and lists of integers as attributes.

    The output dictionary has as keys the keys common to at least half
    of the dictionaries of the input list.  Each x key of this output
    dictionary is associated with a set.  An integer is present in the
    set with key x if and only if it is present in the attribute list
    of key x for at least one dictionary in dictionariesList.

    For example:
    - if dictionariesList contains the three dictionaries
    {'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}
    the returned dictionary will be
    {'a':{1,2,3,5},'b':{2,3},'d':{3,4}}

    '''
    keys = {}
    for dic in dictionariesList:
        k = list(dic.keys())
        for i in k:
            if i in keys:
                keys[i] += 1
            else:
                keys[i] = 1
    least = (len(dictionariesList)+1) // 2
    new_keys = {}
    for a,b in keys.items():
        if b>=least:
            new_keys[a] = []
    for i in dictionariesList:
        for j in list(i.keys()):
            if j in list(new_keys.keys()):
                new_keys[j].extend(i[j])
    new_keys = {a:(set(b)) for a,b in new_keys.items()}


    return(new_keys)
    print(keys)
es37([{'a': [1,3,5],'b':[2,3 ],'d':[3]},
    {'a':[5,1,2,3], 'b':[2],'d':[3]},
    {'a':[3,5], 'c':[4,1,2],'d':[4]}])











