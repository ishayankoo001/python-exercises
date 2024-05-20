def es33(fname1, fname2):
    '''Design and implement the function es33(fname1,fname2) which takes
    as input the path to a text file fname1 and builds a histogram
    with the frequencies of some of the characters in the text
    file. The function also saves the created histogram in the fname2
    text file and returns the number of lines it is composed of.  The
    histogram contains as many lines as the number of characters
    between 'a' and 'z' found in the text of fname1.  If a certain
    character x appears in the text y times, then in the histogram
    there will be a row with a string composed of y repetitions of the
    x character. The rows of the histogram must be ordered by
    decreasing length of the characters that appear in the histogram
    and in alphabetical order, in case of equal length.

    For example if the file  fname1 contains the text 'Monti, Sterbini
    e Spognardi' then the value returned by the function will be 11
    and the histogram will be

    iiii
    nnn
    ee
    oo
    rr
    tt
    a
    b
    d
    g
    p

    '''
    with open(fname1) as f:
        whole = f.read()
        whole.strip()
        ls = [i for i in whole if i.isalpha() and i.islower()]
        dict = {}
        for i in ls:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        dict = sorted(dict.items(), key=lambda x: [-x[1], x[0]])
    with open(fname2, "w") as f2:
        h = 0
        for i, v in dict:
            f2.write(i * v)
            h += 1
            if h != len(dict):
                f2.write("\n")
    return len(dict)

