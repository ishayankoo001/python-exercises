import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ftesto, expectedMatrice, expectedCornice):
        '''Test implementation
            - ftesto             : text file
            - expectedMatrice    : expected matrix
            - expectedCornice    : expected frame value
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es19(ftesto)
        m, c = result
        self.assertEqual(type(result),  tuple, "The result is not a tuple")
        self.assertEqual(len(result),  2, "The tuple must have two elements")
        self.assertEqual(
            m, expectedMatrice, f"The result must be {expectedMatrice} instead of {m}")
        self.assertEqual(
            c, expectedCornice, f"The result must be {expectedCornice} instead of {c}")

    @data(
        ('fm10_1.txt', [[1, 20,  3, 40,  5],
                        [60,  7,  8,  9, 10],
                        [11, 12, 13, 14, 15]], 204),
        ('fm10_2.txt', [[1],
                        [2],
                        [3],
                        [4],
                        [5]], 15),
        ('fm10_3.txt', [[1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5],
                        [1, 2, 3, 4, 5]], 54)
    )
    @unpack
    def test(self, ftesto, expectedMatrice, expectedCornice):
        return self.do_test(ftesto, expectedMatrice, expectedCornice)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
