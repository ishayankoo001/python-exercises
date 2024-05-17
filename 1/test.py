import testlib
import isrecursive
import tree
import json
import random
from ddt import file_data, ddt, data, unpack

import program

@ddt
class Test(testlib.TestCase):

    def do_test(self, list1, list2, expected):
        '''Test implementation:
            - list1: list of nodes in input tree1
            - list2: list of nodes in input tree2
            - expected: the output tree’s nodes list
        '''
        # Check recursion

        tree1 = tree.BinaryTree.fromList(list1)
        tree2 = tree.BinaryTree.fromList(list2)
        try:
            isrecursive.decorate_module(program)
            program.ex1(tree1, tree2)
        except isrecursive.RecursionDetectedError:
            pass
        else:
            raise Exception("Missing recursion")
        finally:
            isrecursive.undecorate_module(program)
        
        with self.ignored_function('builtins.print'), \
             self.forbidden_function('os.walk'):
             #self.timer(2):
            result = program.ex1(tree1, tree2)
            print(result)
        
        self.assertEqual(list1, tree1.toList(), "Tree1 was modified")
        self.assertEqual(list2, tree2.toList(), "Tree2 was modified")
        self.assertEqual(result.toList(), expected, "Returned tree is incorrect")

    def test_1(self):
        '''
        Test with the following two input trees:

                    9                          4                                        145
                  /  \                       /  \                                      /  \
                 /    \                     /    \                                    /    \
                /      \                   /      \                                  /      \
               /        \                 /        \                                /        \
              /          \               /          \                              /          \
             2            4             4            4    The result should be:   63          69
           /  \         /   \         /   \        /   \                        /   \        /  \
        6     6       6      6       5     6      7     8                     28    29     30   31
       / \   / \    / \     / \     / \   / \    / \   / \                   / \   / \    / \   / \
      5   5 5   5  5   5   5   5   1   6 6   1  1   6 6   1                 6  11 11  6  6  11 11  6
        '''
        list1 = [9,[2,[6,[5, None, None],[5, None, None]],[6,[5, None, None],[5, None, None]]],
        [4,[6,[5, None, None],[5, None, None]],[6,[5, None, None],[5, None, None]]]]
        list2 = [4,[4,[5,[1, None, None],[6, None, None]],[6,[6, None, None],[1, None, None]]],
            [4,[7,[1, None, None],[6, None, None]],[8,[6, None, None],[1, None, None]]]]
        list3 =[145, [63, [28, [6, None, None], [11, None, None]], [29, [11, None, None], [6, None, None]]], 
        [69, [30, [6, None, None], [11, None, None]], [31, [11, None, None], [6, None, None]]]]
        return self.do_test(list1, list2, list3)

    def test_2(self):
        '''Test with the following two input trees:
            
            5              1                                             30      
            \              \                                             \     
            1              5                                             24
            /              /                                             /     
            5              1          The result should be              18
            \              \                                             \
            1              5                                             12    
            /              /                                             /
            5              1                                             6
        '''
        list1 = [5,None,[1,[5,None,[1,[5,None,None],None]],None]]
        list2 = [1,None,[5,[1,None,[5,[1,None,None],None]],None]]
        list3 = [30, None, [24, [18, None, [12, [6, None, None], None]], None]]
        return self.do_test(list1, list2, list3)
    
    def test_3(self):
        '''Prova con in input i due alberi:
            
                 1              7                                    90
                /\             /\                                    /\   
               2  3           1  3                                  76 6
              / \            / \                                   / \
             4   5          4   6     The result should be       36  37
           /    /          /   /                                 /   /
          6    7          5   2                                 28 26
         /     \         /    \                                /    \
        8      9       9      8                              17    17    
        

        '''
        list1 = [1, [2, [4, [6, [8, None, None], None], None], [5, [7, None, [9, None, None]], None]], [3, None, None]]
        list2 = [7, [1, [4, [5, [9, None, None], None], None], [6, [2, None, [8, None, None]], None]], [3, None, None]]
        list3 = [90, [76, [36, [28, [17, None, None], None], None], [37, [26, None, [17, None, None]], None]], [6, None, None]]
        return self.do_test(list1, list2, list3)

if __name__ == "__main__":
    Test.main()