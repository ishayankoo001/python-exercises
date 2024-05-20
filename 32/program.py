import json


def ex32(fname1):
    '''Design and implement a function ex32(fname1) such that:
    - it takes as argument the path of a json file.  The json file
    contains a list of strings and each string is composed of by
    decimal digits
    - it returns a list of integers.
    The returned list has many elements as the original list, but each
    string is replaced by a tuple of two integers.
    The first element of the tuple is the sum of the odd digits of the
    string. The second element of the tuple is the sum of the even
    digits of the string.

    Example: if 'fname1' contains the list
    ['11','24','134','1','2876'], the function will return the list
    [(2,0), (0,6), (4,4), (1,0), (7,16)]

    '''
    with open(fname1) as f:
        js = json.load(f)
        newls = []
        for element in js:
            a = sum(int(a) for a in element if int(a) % 2 == 0)
            b = sum(int(a) for a in element if int(a) % 2 != 0)
            newls.append((b,a))


        return newls


print(ex32("file1.json"))
# insert here your code
