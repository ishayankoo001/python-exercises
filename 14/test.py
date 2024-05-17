
# test example

# needed imports
import copy
import testlib
import json
import random
from ddt import file_data, ddt, data, unpack
import isrecursive
import bintree

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, lista, x, expected):
        '''Test implementation
            - lista         : list of binary tree nodes
            - x             : integer number
            - expected      : number of nodes with divisible value for x
        '''
        tree = bintree.BinTree.fromList(lista)
        try:
            isrecursive.decorate_module(program)
            program.es14(tree, x)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Recursion not present")
        finally:
            isrecursive.undecorate_module(program)
        tree = bintree.BinTree.fromList(lista)
        # poi controlliamo che faccia quello che deve fare
        # - ignoraando la presenza di stampe
        # - proibendo l'uso della funzione os.walk
        # - con un timeout di 2 secondi
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.es14(tree, x)
        self.assertEqual(type(result), int, "The result is not an integer")
        self.assertEqual(result, expected, f"Result must be {expected} instead of {result}")

    @data(  
            ([7, [1, [4, [5, [9, None, None], None], None], [6, [2, None, [8, None, None]], None]], [3, None, None]], 2, 3),
            ([9, [2, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]], [4, [6, [5, None, None], [5, None, None]], [6, [5, None, None], [5, None, None]]]], 1, 7),
            ([5,None,[2,[5,None,[1,[5,None,None],None]],None]], 1, 3)
        )
    @unpack
    def test(self, lista, x, expected):
        return self.do_test(lista, x, expected)
        
# Tests are performed both executing program.py and calling  pytest in the directory
if __name__ == '__main__':
    Test.main()

