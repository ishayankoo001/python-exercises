

def es64(l):
    '''
    Write the es64 function which takes as input a list of non-negative integers.
    The function has to produce a string containing the numbers of the list
    vertically aligned, separated by one space and one digit per line. The numbers
    should be aligned so that their unit digits are on the same bottom line.

    Ex: es64([5,69,2090]) returns the string
        2
        0
      6 9
    5 9 0
    '''
    max_len = len(str(max(l)))
    mystr = ""
    l = [str(i) for i in l]
    for i in (range(max_len,0,-1)):
        for j,val in enumerate(l):
            if len(str(val)) == i:
                if(j==len(l)-1):
                    mystr += str(val)[0]
                else:
                    mystr += str(val)[0] + " "
                try:
                 l[j] = (str(val)[1:])
                except ValueError:
                    pass
            else:
                if(j==len(l)-1):
                    mystr += " "
                else:
                    mystr+="  "
        mystr+= "\n"
    return mystr[:-1:]




print(es64([1, 23, 2000]))
print("    2\n    0\n  2 0\n1 3 0")

