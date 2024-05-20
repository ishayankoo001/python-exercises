def ex30(fname1, fname2, fname3):
    '''Design and implement a function ex30(fname1,fname2,fname3) such that:
    - it takes as arguments the paths of three text files
    - it transforms the content of the 'fname1' file using an encoding
      defined in the 'fname2' file and writes the result in the
      'fname3' file
    - it returns the number the number of characters decoded with the
      symbol '?' and saved in the decoded 'fname3' file.
    The first 'fname1' text file contains an encoded message where
    each character was replaced by a three-digit integer. Any
    non-numeric character was not encoded and should be reported as it
    is in the 'fname3' file.
    The second 'fname2' text file contains the characters-number
    encoding of the characters in 'fname1'. The content of 'fname2'
    file is organized in lines. Each line contains one character and
    the three-digit integer that was used to encode that character in
    'fname1', separated by at least one space.  Different numbers can
    refer to the same character and not all the numbers that appear in
    'fname1' eventually appear in the decoding 'fname2' file.  The
    numbers not present in the second file should be decoded with the
    '?' symbol and saved in the 'fname3' file.

    Example: if the fname1 file contains the text
             '991118991991345    103 091027003091103?' and
             the fname2 file contains the text
             'n   091\n   t 991\n a   103\n a 127\n n 003\n  u 118 ', then
             the decoded message to be save in file3 will be:
             'tutt? a n?nna?' and the function returns the value 2.


             008 001 007 009005006008007004 002010003011004!
    '''
    # insert here your code
    with open(fname2) as f:
        dict = {}
        for line in f:
            print(line)
            dict[line.strip()[-3:]] = line.strip()[0:-3].strip()
        f.close()
    print(dict)
    with open(fname1) as f:
        with open(fname3,"w") as fw:
            sums = 0
            a = f.readline()
            lists = []
            for i,val in enumerate((a)):
                if val.isnumeric():
                    lists.append(val)
                    if len(lists)==3:
                        code = "".join(lists)
                        if code in dict:
                            fw.write(dict[code])
                        else:
                            fw.write("?")
                            sums+=1
                        lists = []


                else:
                    fw.write(val)

        print(dict)
        return sums


ex30("ftesto2.txt", "ftesto2b.txt", "test.txt")
