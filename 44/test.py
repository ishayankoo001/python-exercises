import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, a, b, expected):
        '''Implementation of the test
            - a : number of items to find
            - b : number of dividers
            - expected : expected set
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es44(a, b)
        self.assertEqual(type(result), set, "The result is not a set")
        self.assertEqual(result, expected, f"The result must be {expected} instead of {result}")


    @data(
        (20, 2, {2, 3, 67, 5, 37, 7, 71, 41, 11, 43, 13, 47, 17, 19, 61, 53, 23, 59, 29, 31}),
        (10, 3, {289, 4, 9, 169, 361, 841, 49, 529, 121, 25}),
        (10, 4, {33, 6, 8, 10, 14, 15, 21, 22, 26, 27})
    )
    @unpack
    def test(self, a, b, expected):
        return self.do_test(a, b, expected)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
