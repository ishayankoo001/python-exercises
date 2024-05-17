import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fjson, k, expected):
        '''Test implementation
            - fjson         : JSON file containing the matrix
            - k             : side of the square
            - expected      : expected square position
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es40(fjson, k)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        ('f5a.json', 1, (0, 3)),
        ('f5b.json', 6, (-1, -1)),
        ('f5b.json', 5, (4, 2))
    )
    @unpack
    def test(self, fjson, k, expected):
        return self.do_test(fjson, k, expected)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
