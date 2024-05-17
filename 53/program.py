

def es53(ftesto):
    '''Design the function es53(ftext) that,
    - receives as an input the path of a text file and
    - returns a dictionary in which the keys are integer and the
      values are integer lists.

    The dictionary to be returned has to be read from the text file in
    input. The dictionary is stored as a sequence of integers separated
    by an  arbitrary number of spaces (' '), new line characters ('\n')
    and colons (':').
    Dictionary keys are always followed by ':' and then by the related
    list of elements.

    As an example:
    if the file contains the text
    '' 
    3 : 3 6 9
    2: 4 6 10
    ''
    the function will return the dictionary { 3: [3,6,9], 2: [4,6,10]}
    if the file contains 
    ''     4: 5 6: 7        8 
    9 10 11:12 13:14 
    15'' 
    the function will return the dictionary {4:[5], 6:[7,8,9,10], 11:[12], 13:[14,15]}
    '''
    # insert here your code


