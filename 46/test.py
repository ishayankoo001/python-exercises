import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, parola, expected):
        '''Test implementation
            - word      : character string
            - expected  : expected string palindrome 
        '''
        word1 = word
        try:
            isrecursive.decorate_module(program)
            program.es46(word1)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)

        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es46(word)
        self.assertEqual(type(result), str, "The result is not a string")
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")

    @data(
        ("zzzcdcaaabvv", "aaa"),
        ("adbbabbcbbaad", "abbcbba"),
        ("monti_sterbini_spognardi", "ini")
    )
    @unpack
    def test(self, word, expected):
        return self.do_test(word, expected)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
