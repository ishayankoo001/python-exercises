import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, text, expected):
        '''Test implementation
            - text    : text file containing a dictionary
            - expected : expected dictionary
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es53(text)
        self.assertEqual(type(result), dict,
                         "The result is not a dictionary")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        ('ftext10_1.txt', {1: [3, 4, 5], 6: [6, 7], 8: [9]}),
        ('ftext10_2.txt', {1: [3, 4, 5], 6: [6, 7],
                            8: [9, 10, 13], 5: [1, 6], 7: [21]}),
        ('ftext10_3.txt', {1: [2, 3, 4, 4], 6: [7],
                            8: [9, 10, 11, 12, 13], 14: [15, 16, 17, 18]})
    )
    @unpack
    def test(self, text, expected):
        return self.do_test(text, expected)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
