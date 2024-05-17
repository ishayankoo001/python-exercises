import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, labyrinth, expected, expectedLab):
        '''Test implementation
            - labyrinth     : labyrinth as a list of lists form
            - expected      : position of the expected position
            - expectedlab   : check that the matrix has not changed
        '''
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es38(labyrinth)
        self.assertEqual(
            result, expected, f"The result must be {expected} instead of {result}")
        self.assertEqual(
            labyrinth, expectedLab, "The original labyrinth has been modified")

    @data(
        ([[0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0], [0, 0, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0], [
         0, 0, 1, 1, 0, 1, 0], [1, 0, 0, 1, 0, 1, 1], [0, 1, 1, 0, 1, 0, 0]], (4, 5)),
        ([[0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]], (7, 6))
    )
    @unpack
    def test(self, lab, expected):
        return self.do_test(lab, expected, lab)


# The tests are performed either by running program.py or by calling pytest from the directory
if __name__ == '__main__':
    Test.main()
