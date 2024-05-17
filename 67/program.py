import os
import os.path


def es67(path):
    """WARNING: it's FORBIDDEN to use the os.walk function or other
    library functions that allow to search all the files in a
    directory (you have to explore the directory)

    Define the recursive function (or a function that uses your
    recursive functions) es67 that:
    - receives as input the pathname of a directory and
    - recursively explores the corresponding directory and returns a
    dictionary.

    NOTE: all files and directories starting with '.' should be ignored.

    The dictionary has the file extensions found in the directory as its key
    (i.e. the last 3 characters of the file name, ex: 'txt', 'pdf', 'png').
    The value associated with each key K is the distance (difference in depths)
    between the deepest file that has that extension and the shallowest.
    Assume that the files contained in the input directory are at depth 0.
    Example:
    if in the directory with path='A1' there are only two files of type 'txt'
        A1/a/b/c/d/e/f/g/h/pippo.txt    at depth 8    (counting A1 = 0)
        A1/d/f/pappo.txt                at depth 2
        result contains the pair key: value
        'txt' : 6

    """
    # insert here your code
