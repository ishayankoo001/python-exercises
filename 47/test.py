import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, string_list, expected, expectedLst):
        '''
        Implementation of the test
            - list : input list
            - expected : awaited sorted list
            - expectedLst : same as the input list to verify that it has not been changed
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es47(string_list)
        self.assertEqual(type(result), list, "The result is not a list")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.assertEqual(
            string_list, expectedLst, f"The input list has been modified")

    @data(
        (['uuu', 'ccc', 'a', 'aa', 'd', 'z', 'zzz', 'uuu', 'z',
          'z', 'uuu'], ['z', 'd', 'a', 'aa', 'zzz', 'uuu', 'ccc']),
        (['a', 'a', 'bb', 'bb', 'ccc', 'ccc', 'dddd', 'dddd',
          'eeeee', 'eeeee'], ['a', 'bb', 'ccc', 'dddd', 'eeeee']),
        (['a', 'b', 'c', 'd', 'rr', 'ss', 'ttt', 'uuu', 'vv', 'n', 'm', 'l'],
         ['n', 'm', 'l', 'd', 'c', 'b', 'a', 'vv', 'ss', 'rr', 'uuu', 'ttt'])
    )
    @unpack
    def test(self, string_list, expected):
        return self.do_test(string_list, expected, string_list)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
