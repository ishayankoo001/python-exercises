def ex24(filename, char_list):
    '''Design a function ex24(filename, char_list) such that:
    - it takes as argument the name of a file 'filename' and a list of
    characters 'char_list'
    - it returns a ordered list of tuples (character, string).
    For each character in the character list, the function computes
    the percentage of occurrences in the content of the file, ignoring
    the distinction between uppercase and lowercase.
    The first element of each tuple is a character of the list, while
    the second element is a string representing the percentage
    w.r.t. the total number of alphabetic characters (those for which
    the method isalpha() returns True) contained in 'filename'. The
    string should have the percentage rounded to the second decimal
    place and should end with the '%' character.
    The returned list of tuples is ordered in descending order of
    percentage, and in case of tie, in alphabetical order.

    Example: if 'filename' contains the sequence of characters
    'sono proprio cOntentO', and char_list=['o','i', 'S'], the
    function returns the list
    [('o', '31.58%'), ('S', '5.26%'), ('i', '5.26%')]
    '''
    pass
