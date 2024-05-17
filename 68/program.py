import os
import os.path

def es68(dirname, extensions):
    """Design a function es68(dirname, extensions) such that:
    - it is recursive or uses recursive functions(s)/method(s),
    - it receives as arguments:
      - a directory pathname 'dirname', 
      - a list of strings 'extensions' representing the ending part of
         filenames, a list of strings 'words' that do not contain
      - spaces/tab/newlines
    - it counts how many files ending with any of the given extensions
      can be found in 'dirname' or any of its subdirectories.
    - it returns a dictionary where:
      - the keys are the extensions passed as argument, if at least
        one file ending with such an extension can be found, and
      - the related values are the number of files whose name ends
        with such a keys.

    Note: if no file can be found ending with a given extension, such
    a key is not included in the returned dictionary.
    """
    # insert here your code
    dict = {ext:0 for ext in extensions}
    for f in os.listdir(dirname):
        fn = os.path.join(dirname,f)
        if os.path.isdir(fn):
            diz = es68(fn,extensions)
            for a,b in diz.items():
                dict[a]+=b
        else:
            for x in extensions:
                if fn.endswith(x):
                    dict[x] += 1
    for n in list(dict.keys()):
        if dict[n]==0:
            del dict[n]
    return dict





