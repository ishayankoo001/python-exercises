import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, f1, f2, expected, expectedIsto):
        '''Test implementation
            - f1            : text file
            - f2            : file where to save the histogram
            - expected      : number of histogram rows
            - expectedIsto  : expected histogram
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es33(f1, f2)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        with open(f2, 'r', encoding='utf8') as f:
            testo = f.read()
        self.assertEqual(
            testo, expectedIsto, f"Histogram must be {expectedIsto} instead of {testo}")

    @data(
        ('ftesto3.txt', 'istogramma1.txt', 11,
         'iiii\nnnn\nee\noo\nrr\ntt\na\nb\nd\ng\np'),
        ('ftesto4.txt', 'istogramma2.txt', 20, 
         'aaaaaaaaaaaaaaaaaaaaa\noooooooooooooooooooo\neeeeeeeeeeeeeeee\niiiiiiiiiiiiii\nrrrrrrrrrrrrrr\nnnnnnnnnnnnnn\nuuuuuuuuu\nssssssss\nmmmmmmm\nllllll\npppppp\nddddd\nttttt\ncccc\nhhh\nbb\nff\nvv\nzz\ng')
    )
    @unpack
    def test(self, f1, f2, expected, expectedIsto):
        return self.do_test(f1, f2, expected, expectedIsto)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
