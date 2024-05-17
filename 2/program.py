
def es2(ls,ftext):
   '''Design and implement the function es4(ls,ftext) that
   - takes:
      - a list 'ls' containing strings of characters
      - a text file path 'ftext' containing at least two character
        strings separated by spaces and/or commas and/or new line
        character
   - modifies the list 'ls' deleting from it all the strings that is
      possible to obtain as a concatenation of two consecutive strings
      read from the file 'ftext'
   - returns the number of strings deleted from ls.

   EXAMPLE: 
   if ls=['b', 'abba', 'babc','ccc', 'bba', 'bb' ] and the content of
   ftext file is the sequence "b, \n\n\n ab  ba, b \nc c cc",
   then, the es2 function returns 2
   and the ls list will be modified as ['b',  'babc', 'bba', 'bb' ].
   In facts, the file contains the sequence of strings
   'b', 'ab', 'ba', 'b', 'c' 'c' 'cc'
   and the strings in ls that can be obtained as a concatenation of
   two words that appear one after the other in the text file are:
   'abba' = 'ab' +'ba'
   'ccc'= 'c' + 'cc'

   '''
   #enter your code here
