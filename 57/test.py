import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, grid, expected):
        '''Implementation of the test
            - grid : matrix of integers in the form of a list of lists
            - expected : tuple of 4 lists
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es57(grid)
        self.assertEqual(type(result), tuple, "The result is not a tuple")
        self.assertEqual(
            result, expected, f"The result should be {expected} instead of {result}")

    @data(
        ([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]],
         ([2, 2, 2, 1], [1, 2, 2, 2], [3, 2, 1, 4], [4, 1, 2, 3])),
        ([[1, 2, 3, 4], [4, 1, 'c', 3], [3, 4, 1, 2], [2, 3, 4, 1]], ([], [], [], [])),
        ([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 2, 1], [2, 3, 4, 1]], ([], [], [], [])),
        ([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 6, 1]], ([], [], [], [])),
        ([[3, 2, 1, 4], [2, 3, 4, 1], [1, 4, 3, 2], [4, 1, 2, 3]],
         ([2, 3, 2, 1], [1, 2, 3, 2], [1, 2, 3, 2], [2, 3, 2, 1])),
        ([[3, 2, 1, 4], [1, 3, 4, 2], [2, 4, 3, 1], [4, 1, 2, 3]],
         ([2, 3, 2, 1], [1, 2, 3, 2], [1, 2, 3, 2], [2, 3, 2, 1]))
    )
    @unpack
    def test(self, grid, expected):
        return self.do_test(grid, expected)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or by calling pytest in the directory
if __name__ == '__main__':
    Test.main()
