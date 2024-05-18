
def unvowelized(word):
    vowels = ["a", "e", "i", "o", "u"]
    word = "".join([x for x in word if x not in vowels])
    return word

def ex11(textfile):
    '''Design a function ex11(textfile) such that:
      - it receives as argument the path of a text file that contains
        in each line a distinct string of characters
      - it returns a dictionary having strings as keys and string lists as
        values.
      The dictionary keys are the strings contained in the 'textfile',
      without any vowel and with the remaining characters sorted in
      alphabetical order (for example, the string 'angel' generates the
      key 'ngl').
      The corresponding value of a key is the list of strings of
      'textfile' that generated that key (note that different strings can
      generate the same key as for 'car', 'core' and 'cure').  The strings
      in the list are sorted by decreasing length and, with equal lengths,
      in alphabetical order.

      Example: for the text file f10.txt, the function returns the
      dictionary:
         {'prt': ['parto', 'porta'],
         'r': ['era', 'ora'],
         'pr': ['arpia', 'arpa'],
         'cs': ['casa', 'cosa'],
         'fll': ['follia', 'fallo', 'folla'],
         'rt': ['otre', 'tre'],
         'lp': ['piolo', 'polo']
         }
    '''
    words = []
    with open(textfile) as f:
        for line in f:
            if line.strip() != '':
                words.append(line.strip())
    print(words)
    dict = {}
    for word in words:
        if unvowelized(word) in dict:
            dict[unvowelized(word)].append(word)
        else:
            dict[unvowelized(word)] = [word]
    dict = {"".join(sorted([w for w in k], reverse=False)):sorted(v, key = lambda x:[-len(x), x]) for k,v in dict.items()}


    return dict

print(ex11("ft10a.txt"))



