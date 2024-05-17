import copy

def ex54(mylist):
    '''Design a function ex54(mylist) such that:
    - it receives as arguments a list containing integers and strings
    - it modifies the list by deleting all the strings
    - it returns a dictionary.
    The function deletes from 'mylist' all the elements that are
    strings and returns a dictionary where:
    - the keys are the deleted strings
    - the values are the number of times the related key-string was
      deleted from 'mylist'.
    The use of the library copy is allowed.

    Example: if mylist=[1,'a',2,'b','a',8,'d',8], the function returns
    the dictionary {'a':2,'b':1,'d':1} and the list becomes [1,2,8,8]

    '''
    # insert here your code
    new_list_nums = [x for x in mylist if isinstance(x, int)]
    new_list_chars = [x for x in mylist if isinstance(x, str)]
    mylist[:] = new_list_nums
    dict = {}
    for i in new_list_chars:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


