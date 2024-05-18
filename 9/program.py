import os

def ex9(pathDir):
    '''Define a function ex9(pathDir) such that:
        - it is recursive or uses recursive functions(s)/method(s);
        - it receives the pathname 'pathDir'of a directory as argument;
        - it returns a list of pairs (tuple with two elements). Each tuple
          contains the name of a subdirectory that can be reached from
          'pathDir' and the total amount of bytes of all the files with
          extension .txt is that subdirectory.
        The list are sorted in descending order with respect to their
        second component (the amount of bytes of the .txt files) and, in
        case of tie, in alphabetical order with respect to the first
        component (the name of the subdirectory).  Files and directories
        whose name begins with the '.'  character should not be
        considered.

        For the purposes of the exercise, the following may be useful the
        following functions in the os module: os.listdir(),
        os.path.isfile(), os.path.isdir(), os.path.basename(),
        os.path.getsize()

        Example: with es9('Informatica/Software') it is returned the list:
        [('SistemiOperativi', 287), ('Software', 10), ('BasiDati', 0)]

    '''
    # insert your code here
    list = []
    explorer(pathDir,list,())
    list = [x for x in list if x != ()]
    list = sorted(list, key = lambda x: [-x[1],x[0]])
    print(list)
    return list

def explorer(pathDir, mylist, mytuple):
    sum = find_text_size(pathDir)
    mylist.append((os.path.basename(pathDir), sum))
    for f in os.listdir(pathDir):
        fn = os.path.join(pathDir, f)
        if os.path.isdir(fn):
            mylist.append(explorer(fn, mylist, mytuple))

    return mytuple
def find_text_size(path):
    sum = 0
    for f in os.listdir(path):
        fn = os.path.join(path,f)
        if os.path.isfile(fn):
            if fn.endswith(".txt"):

                sum += os.path.getsize(fn)
    return sum
(ex9('Informatica/Software'))




                
    
        
