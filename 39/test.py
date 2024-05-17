import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, n, fjson, expected, expectedJson):
        '''Test implementation
            - n : spiral matrix order
            - fjson : json file where to save the matrix
            - expected : sum of the even columns of the matrix
            - expectedJson : json file to check the correctness of the matrix
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex39(n, fjson)
        self.assertEqual(
            result, expected, f"Il risultato deve essere {expected} invece che {result}//The result should be {expected} instead of {result}")
        self.check_json_file(fjson, expectedJson)

    @data(
        (4, 'f4a.json', 74, 'Ris4a.json'),
        (10, 'f4b.json', 2569, 'Ris4b.json')
    )
    @unpack
    def test(self, n, fjson, expected, expectedJson):
        return self.do_test(n, fjson, expected, expectedJson)


# The tests can be performed running program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
