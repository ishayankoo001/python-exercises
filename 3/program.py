def es3(set1, set2):
    '''
    Design a function ex3(set1, set2) that:
    - takes two sets of natural numbers as input,
    - finds all triples (a,b,c) such that:
      - a, b and c are in set1
      - a < b < c and
      - (a + b + c) is in set2
    - returns the set of all such triples.
    Notice that the returned triples should be represented as tuples in a list. Those
    tuples should be sorted based on the sum of their components in ascending
    order. If two tuples map to an equivalent sum, they should be sorted by ascending
    lexicographic order.
    EXAMPLE:
    Given set1={2, 4, 5, 6, 8, 9} and set2={5, 15, 19, 25}, the function returns the
    following list:
    [(2, 4, 9), (2, 5, 8), (4, 5, 6), (2, 8, 9), (4, 6, 9), (5, 6, 8)]
    '''

    nums = []
    set1 = list(set1)
    print(set1)
    set2 = list(set2)
    for i in range(0,len(set1)-2):
        for j in range(i+1,len(set1)-1):
            for k in range(j+1,len(set1)):
                if set1[i]+set1[j]+set1[k] in set2:
                    nums.append((set1[i],set1[j],set1[k]))
    nums.sort(key=lambda x:(sum(x),x))
    return nums

set1 = {2, 4, 5, 6, 8, 9}
set2 = {5, 15, 19, 25}
print(es3(set1,set2))
