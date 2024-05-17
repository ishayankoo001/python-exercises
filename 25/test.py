import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, n, expected):
        '''Test implementation
            - n             : row number of the triangle of Tartaglia
            - expected      : expected list of integers
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es25(n)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        (1, [1, 1]),
        (3, [1, 3, 3, 1]),
        (9, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])
    )
    @unpack
    def test(self, n, expected):
        return self.do_test(n, expected)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
