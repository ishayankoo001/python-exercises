

import os
def es80(dir1, words):
    '''WARNING: use as file separator the character "/" that works in both
                Windows and Linux or the os.path.join function
       WARNING: it is forbidden to use the os.walk function.

    Design a function es80(dir1, words) such that it receives as arguments:
      - dir1: the path of a directory
      - words: a set of words (strings of character between 'a' and 'z')
    and does the following:
      - it searchs in the dir1 directory and in its subdirectories
        files with extension .txt containing strings belonging to the
        'words' set
      - it returns a dictionary with the found words.
    In the returned dictionary, the keys are the found words and the
    related values are tuples of two integers.
    The first element of the tuple is the total number of times the
    word has been found in any .txt file.  The second element of the
    tuple is the maximum depth of the files in which the word can be
    found. The depth of the files in the directory dir1 is 0.
    Remember that a word is a maximal sequence characters between 'a'
    and 'z'.  Assume that all .txt files in dir1 contain only words
    separated by spaces, tabs or new lines (\n) and that there are no
    uppercase characters or punctuation marks.

    '''
    # insert your code here
    pass
