 
def es31(fname1,fname2):
    '''Design and implement the function es31(fname1,fname2) which takes
    as input the address of two text files.
    The function modifies the text of fnam1 file as follows:
    - each character between 'a' and 'z' (lowercase) that appears in
    the file in an odd number of words (a word is a maximal sequence
    of characters other than space, tab or new line character) is
    replaced by the corresponding uppercase character.
    The function saves the modified text a new file with path fname2.
    The function returns how many of the 26 characters between 'a' and
    'z' have been modified from lowercase to uppercase in the text.
    For example if
    - the fname1 file contains the text 'Monti, Sterbini e Spognardi'
    - the fname2 file will contain the text 'MoNtI, SterBINI e SPoGNArDI'
    and the function will return the value 7, since the changed
    letters are NIBPGAD.

    '''
    words = []
    changes = []
    with open(fname1) as f:
        for line in f:
            words.extend(line.strip().split())
        chars = [chr(i) for i in range(97,97+26)]
        sums = 0
        newwords = []
        newwords[:] = words
        for c in chars:
            newlis = sum([c in words[i] for i in range(len(words))])
            if newlis % 2 != 0:
                changes.append(c)
    with open(fname1) as f:
        with open(fname2,"w")as f2:
            for line in f:
                print(line)
                for char in changes:
                    line = line.replace(char, char.capitalize())
                f2.write(line)
    return len(changes)

    # insert here your code






es31("ftesto4.txt","test.txt")
with open("check.txt","w") as check:
    check.write('''SalvE, Ho Una doManda:\nMa lo zERo E' Un nUMERo paRi o diSpaRi?\nSo cHE pUo' SEMbRaRE Una banaliTa', a naSo diREi cHE lo zERo E' Un nUMERo paRi\nMa non SapREi coME GiUSTificaRE la RiSpoSTa.\nConfido nEl voSTRo aiUTo!''')
















 
