import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fileIn, fileOut, expected, expectedMatr):
        '''Test implementation
            - fileIn : files with integer matrix
            - fileOut : file where to save the result
            - expected : number of odd columns
            - expectedMatr : how the matrix should be
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex60(fileIn, fileOut)
        self.assertEqual(type(result), int, "Il risultato non è un intero/The returned value is not an int")
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}/The result should be {expected} instead of {result}")
        self.check_text_file(fileOut, expectedMatr)

    @data(
        ('matrice1.txt', 'matrice1Ris.txt', 3, 'matrice1RisCheck.txt'),
        ('matrice2.txt', 'matrice2Ris.txt', 4, 'matrice2RisCheck.txt')
    )
    @unpack
    def test(self, fileIn, fileOut, expected, expectedMatr):
        return self.do_test(fileIn, fileOut, expected, expectedMatr)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
