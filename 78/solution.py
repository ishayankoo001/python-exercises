
def es78(word):
    if len(word)==1: return [word]
    a=word[0]
    _list= es78(word[1:])
    list1=_list[:]
    if a not in list1: list1+=[a]
    for y in _list:
        if a<=y[0] and a+y not in list1: list1+=[a+y]
    return sorted(list1)




