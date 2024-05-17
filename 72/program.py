import os
import json
import os.path


def es72(dirname, jsonFile):
    """Design a function es72(dirname, jsonfile) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as arguments a directory pathname 'dirname' and a
      file name 'jsonfile', and
    - it builds a dictionary representing the structure of 'dirname'
    - it saves the built dictionary as a Json file with name 'jsonfile' 
    - it returns the maximum number of files/directories contained in
      one of the directories/subdirectories
    All files and directories starting with '.' must be ignored.

    The dictionary built by the function is defined as follows:
    - for each file and subdirectory in a directory, the dictionary
      has a key with the name of the file or subdirectory
    - for each key, the related value:
        - is the file size as an integer, if the key is a file;
        - is the dictionary that represents the structure of that
          directory, if the key is a directory.
    The outermost dictionary only contains one key with 'dirname' and
    the related value is the dictionary representing its structure.

    """
    # insert here your code
    pass
