import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, s1, s2, expected):
        '''Implementation of the test
            - s1 : string
            - s2 : string
            - expected : expected list of common substrings
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es45(s1, s2)
        self.assertEqual(type(result), list, "The result is not a set")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        ('aabbccdd', 'acccdzza', ['a', 'c', 'cc', 'ccd', 'cd', 'd']),
        ('python2', 'python3', ['h', 'ho', 'hon', 'n', 'o', 'on', 'p', 'py', 'pyt', 'pyth',
                                'pytho', 'python', 't', 'th', 'tho', 'thon', 'y', 'yt', 'yth', 'ytho', 'ython']),
        ('fondamenti_di_programmazione', 'progettazione_di_algoritmi', ['_', '_d', '_di', '_di_', 'a', 'az', 'azi', 'azio', 'azion', 'azione', 'd', 'di', 'di_', 'e',
                                                                        'g', 'i', 'i_', 'io', 'ion', 'ione', 'm', 'n', 'ne', 'o', 'og', 'on', 'one', 'p', 'pr', 'pro', 'prog', 'r', 'ro', 'rog', 't', 'z', 'zi', 'zio', 'zion', 'zione'])
    )
    @unpack
    def test(self, s1, s2, expected):
        return self.do_test(s1, s2, expected)


# TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
