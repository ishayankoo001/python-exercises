
import os

def find_in_file(file, word):
    words = []
    with open(file) as f:
        for line in f:
            words.extend(line.strip().split(" "))
    occurence = 0
    for w in words:
        if w == word:
            occurence += 1
    return occurence
def es35(dir1, words):
    """Design the function  es35(dir1, word_set), that takes as inputs:
        dir1:   the path of a directory
        word_set:  a set of words (character strings between 'a' and 'z')
    and does the following:

    it searches in dir1 for files with extension .txt that contain any
    string present in word_set and returns a dictionary of the found
    words. The function does not considers dir1 subdirectories.  The
    returned dictionary only contains the words actually found within
    the .txt files in dir1 and the attribute of each key is a tuple of
    two integers. The first element of the tuple is the total number
    of times the word can be found in dir1 .txt files. The second
    element of the tuple is the number of different dir1 .txt files in
    which the word can be found.

    A word is a sequence made of characters between 'a' and 'z'.  All
    dir1 .txt files contain only words separated by spaces, tabs or
    new line characters, namely, there are no capital letters or punctuation
    marks.

    """
    path = dir1
    dict = {k:(0,0) for k in words}
    for subdir in os.listdir(path):
        if os.path.isfile(os.path.join(path,subdir)):
            if(subdir[-4:]==".txt"):

                p = os.path.join(path, subdir)
                for w in words:
                    occurences = find_in_file(p,w)
                    if occurences>=1:
                        dict[w] = (dict[w][0]+occurences,dict[w][1]+1)

                print(subdir)
    print(dict)
    dict = {k:v for k,v in dict.items() if v != (0,0)}
    return(dict)
es35("A",["a"])
