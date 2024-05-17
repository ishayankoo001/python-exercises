import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack

import program


@ddt
class Test(testlib.TestCase):

    def do_test(self, d1, d2, expected):
        '''Implementation of the test
            - d1 : dictionary of a sparse matrix
            - d2 : dictionary of a sparse matrix
            - expected : expected dictionary of a sparse matrix
        '''
        d1_test = d1
        d2_test = d2
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es52(d1, d2)
        self.assertEqual(type(result), dict, "The result is not a dictionary")
        self.assertEqual(d1, d1_test, "Input dictionaries should not be modified")
        self.assertEqual(d2, d2_test, "Input dictionaries should not be modified")
        self.assertEqual(result, expected, f"The result should be {expected} instead of {result}")
 

    @data(
        ({(0,2): 4,(1,0): 1, (1,1): 2, (2,1):8 }, {(0,0): 5,(1,1): 2, (2,2): 5, (1,0):2 }, {(0,2): 4,(1,0): 3, (1,1): 4, (2,1):8, (0,0):5, (2,2):5 }),
        ({(1,1):1,(2,3):2,(1,3):3}, {(1,1):1,(2,2):2,(2,3):3,(1,2):5}, {(1, 1): 2, (2, 3): 5, (1, 3): 3, (2, 2): 2, (1, 2): 5}),
        ({(1,1):5,(1,2):5,(2,1):5,(2,2):5}, {(3,1):1,(4,2):1,(4,3):1,(3,2):1}, {(1, 1): 5, (1, 2): 5, (2, 1): 5, (2, 2): 5, (3, 1): 1, (4, 2): 1, (4, 3): 1, (3, 2): 1})
    )
    @unpack
    def test(self, d1, d2, expected):
        return self.do_test(d1, d2, expected)


  # TESTS ARE TO BE PERFORMED IF YOU PERFORM program.py or calling pytest in the directory
if __name__ == '__main__':
    Test.main()
