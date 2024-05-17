import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, fileJson, filePng, expected, expectedPng):
        '''Test implementation
            - fileJson      : JSON containing the encoded matrix
            - filePng       : where to save the image
            - expected      : expected pixel
            - expectedPng   : expected PNG
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es23(fileJson, filePng)
        self.assertEqual(result, expected,
                         f"The result must be {expected} instead of {result}")
        self.check_img_file(filePng, expectedPng)

    @data(
        ('italia.json', 'o1.png', (0, 255, 0), 'italia.png'),
        ('3cime.json', 'o2.png', (53, 138, 219), '3cime.png')
    )
    @unpack
    def test(self, fileJson, filePng, expected, expectedPng):
        return self.do_test(fileJson, filePng, expected, expectedPng)


# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()
