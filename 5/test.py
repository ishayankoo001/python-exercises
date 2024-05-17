import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, string_set, k, expected):
        # check if recursion is present
        try:
            isrecursive.decorate_module(program)
            program.es5(string_set, k)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        # checks if the function returns the correct value
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es5(string_set, k)
        self.assertEqual(result, expected, "the returned value is not correct")

    def test_1(self):
        '''
        \nFirst es5 function test with k=3 and set={'a','bb','c'}: 
        '''

        expected = {'bbca', 'bbbbbb', 'ccc', 'cca', 'caa', 'ccbb', 'bbaa', 'abbc', 'aac', 
        'abbbb', 'acbb', 'cbbc', 'bbbba', 'bbabb', 'cbba', 'cac', 'bbac', 'acc', 'aabb', 
        'aca', 'bbbbc', 'aaa', 'cbbbb', 'abba', 'bbcbb', 'cabb', 'bbcc'}

        return self.do_test({'a','bb','c'}, 3, expected)
    
    def test_2(self):
        '''\nSecond es5 function test with k=2 and set={'a','bb','c'}: 
        '''

        expected = {'aa','abb','ac','bba','bbbb','bbc','ca','cbb','cc'}

        return self.do_test({'a','bb','c'}, 2, expected)

    def test_3(self):
        '''\nThird es5 function test with k=4 and set={'a','bb','c'}:
        '''

        expected = {'abbbba', 'ccbbbb', 'cabba', 'bbcbbbb', 'acbbbb', 'cabbc', 'bbcabb', 
        'acbbc', 'cbbabb', 'bbabbbb', 'accbb', 'cbbac', 'ccca', 'bbacc', 'aaabb', 'caca', 
        'aabbc', 'ccaa', 'ccac', 'acaa', 'abbac', 'bbbbabb', 'bbcbba', 'ccbba', 'cacc', 
        'bbcca', 'aabba', 'bbbbcc', 'abbcc', 'bbaac', 'cabbbb', 'aacbb', 'bbcbbc', 'acbba', 
        'aacc', 'bbaabb', 'abbbbbb', 'bbbbbbbb', 'caaa', 'bbccbb', 'cbbca', 'bbabbc', 'aaac', 
        'acac', 'abbbbc', 'acabb', 'caac', 'bbcaa', 'bbcac', 'bbaca', 'bbccc', 'cbbbbbb', 
        'bbbbaa', 'ccbbc', 'accc', 'abbabb', 'ccabb', 'bbbbcbb', 'bbacbb', 'caabb', 'acca', 
        'abbca', 'abbcbb', 'aaca', 'cbbbbc', 'cacbb', 'aaaa', 'cccbb', 'cbbcbb', 'cccc', 
        'abbaa', 'bbbbbba', 'bbbbac', 'aabbbb', 'bbbbca', 'cbbcc', 'bbabba', 'bbaaa', 
        'cbbaa', 'bbbbbbc', 'cbbbba'}

        return self.do_test({'a','bb','c'}, 4, expected)

if __name__ == '__main__':
    Test.main()
