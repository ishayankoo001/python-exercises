def es10(ftext,k):
    '''Design and implement the function es10(ftext,k) that takes as input
       a text file path and an integer k, and returns a string with length
       k.

       The input text file contains strings of different length (one per
       line and each line ends with '\n'), as the file f9.txt.

       The k characters of the string returned by the function are
       obtained considering all the strings in ftext that are k character
       long.  The i-th character of the string will be the character that
       appears most frequently as the i-th character of the strings with
       length k in ftext. In case of equal occurrences, the first
       character in alphabetical order among the most frequent characters.
       An empty string will be returned if the text file does not contain
       words with length k.

       As an example, for the text file f9.txt and k=3 the function
       returns the string 'are' because in the f9.txt file there are the
       following 4 strings with length 3: tre due amo ora

    '''
    texts = []
    with open(ftext, "r") as f:
        texts.append(f.readlines())
    a = [x.strip() for a in texts for x in a if len(x.strip()) == k]
    text = ""

    for x in range(k):
        dict={}
        for i in a:
            if i[x] in dict:
                dict[i[x]] += 1
            else:
                dict[i[x]] = 1
        dict = sorted(dict.items(), key=lambda x: (-x[1],x[0]))
        text+=(dict[0][0])
    return text

print(es10("ft9.txt", 3))


