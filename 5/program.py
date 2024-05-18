    
def mixer(string_set,original_set,k):
    if k == 1:
        return string_set
    new_set = set()
    for i in string_set:
        for j in original_set:
            new_set.add(i+j)
    return mixer(new_set,original_set,k-1)
def es5(string_set, k):
    return mixer(string_set,string_set,k)

    '''Design and implement the recursive function es5(string_set, k)
    (or that uses recursive function(s) or method(s)) that:
    - takes as arguments a set of strings and an integer k > 0
    and:
    - finds the different strings that can be obtained as the
      concatenation of k copies of the original strings (the same
      string can be used several times for concatenation).
    - returns as a result the set of strings found.
    EXAMPLES: if string_set = {'a','bb','c'}
    1)  es5(string_set, 1) returns {'a','bb','c'}
    2)  es5(string_set, 2) returns {'aa','abb','ac','bba','bbbb','bbc',
                                    'ca','cbb','cc' }
    3)  es5(string_set, 3) returns
    {'bbca', 'bbbbbb', 'ccc', 'cca', 'caa', 'ccbb', 'bbaa', 'abbc', 'aac',
     'abbbb', 'acbb', 'cbbc', 'bbbba', 'bbabb', 'cbba', 'cac', 'bbac',
     'acc', 'aabb', 'aca', 'bbbbc', 'aaa', 'cbbbb', 'abba', 'bbcbb',
     'cabb', 'bbcc}

    TIP: you can simulate the loop on k with recursion

    '''
    # enter your code here
print(es5({'a','bb','c'},3))
print(len(es5({'a','bb','c'},3)))
expected = {'bbca', 'bbbbbb', 'ccc', 'cca', 'caa', 'ccbb', 'bbaa', 'abbc', 'aac',
        'abbbb', 'acbb', 'cbbc', 'bbbba', 'bbabb', 'cbba', 'cac', 'bbac', 'acc', 'aabb',
        'aca', 'bbbbc', 'aaa', 'cbbbb', 'abba', 'bbcbb', 'cabb', 'bbcc'}



