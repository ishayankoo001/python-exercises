import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ftext, op, sel, expected):
        '''Test implementation
            - ftext     : input matrix
            - op        : operation code {'sum', 'min', 'max'}
            - sel       : selection code {'col', 'row', 'dp', 'ds'}
            - expected  : expected list of integers
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es61(ftext, op, sel)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"The result for the operation {op} and the selector {sel} must be {expected} instead of {result}")

    @data(
        ('matrice4.txt', {'maxrow': [2, 20, 5], 'minrow': [-4, 5, -1], 'sumrow': [-2, 35, 5], 'maxcol': [5,  10, 20], 'mincol': [
         2,  0, -4], 'sumcol': [12, 11, 15], 'maxdp': [10], 'mindp': [-1], 'sumdp': [11], 'maxds': [10], 'minds': [-4], 'sumds': [11]}),
        ('matrice5.txt', {'maxrow': [3, 20, 6, 20], 'minrow': [-4, 5, -1, -8], 'sumrow': [-2, 44, 11, 7], 'maxcol': [5,  10, 20, 20],
                          'mincol': [-8, 0, -7, -1], 'sumcol': [5, 13, 8, 34], 'maxdp': [20], 'mindp': [-1], 'sumdp': [32], 'maxds': [20], 'minds': [-8], 'sumds': [12]})
    )
    @unpack
    def test(self, testo, vector):
        for op in ['max', 'min', 'sum']:
            for sel in ['row', 'col', 'dp', 'ds']:
                self.do_test(testo, op, sel, vector[op+sel])


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
