
# Test example

# IMPORTS NEEDED
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, ls, k, expected, expectedLst):
        '''Test implementation
            - ls         : list of words
            - k             : positive integer
            - expected      : expected number of deleted words
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es17(ls, k)
        self.assertEqual(type(result), int,
                         "The result is not an integer")
        self.assertEqual(result, expected,
                         f"The result must be {expected} instead of {result}")
        self.assertEqual(ls, expectedLst,
                         f"The result must be {expectedLst} instead of {result}")

    @data(
        (['ananas', 'pera', 'banana', 'melone', 'kiwi',
          'albicocca'], 3, 3, ['pera', 'melone', 'kiwi']),
        (['Angelo', 'Andrea', 'Osvaldo', 'Anna',
          'Monica', 'Adele'], 2, 4, ['Angelo', 'Monica']),
        (['uAaa', 'uaAa', 'uaaA', 'Bcc', 'cBc', 'ccB'], 3, 3, ['Bcc', 'cBc', 'ccB'])
    )
    @unpack
    def test(self, ls, k, expected, expectedLst):
        return self.do_test(ls, k, expected, expectedLst)


# Tests are executed both exectuting program.py and calling pytest in the directory
if __name__ == '__main__':
    Test.main()
