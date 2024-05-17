    
def es5(string_set,k):
    return recEs5(string_set, string_set, k)

def recEs5(sourceSet, resSet, k):
    if(k == 1):
        return resSet
    else:
        newSet = set()
        for el1 in sourceSet:
            for el2 in resSet:
                newSet.add(el1+el2) 
        return recEs5(sourceSet, newSet, k-1)
