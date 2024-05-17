
import copy
import random

class BinaryTree:
    def __init__(self, val, sx=None, dx=None):
        self.value = val
        self.sx = sx
        self.dx = dx

#################### HENCEFORTH: FUNCTIONS FOR TESTING ONLY ####################
################# WARNING: DO NOT USE THE FOLLOWING FUNCTIONS ##################

    @classmethod
    def fromList(cls, a_list):
        """
        Build the tree from a list in the following form:
          [value, left, right]
        wherein left and right are other trees or None
        :param a_list: a list [value, left, right]
        :return: a tree
        """
        value, sx, dx = a_list
        if sx: sx = cls.fromList(sx)
        if dx: dx = cls.fromList(dx)
        return cls(value, sx, dx)

    def toList(self):
        """
        Convert this tree into a list in the following form:
          [value, left, right].
        :return: a list [value, left, right]
        """
        sx = None if not self.sx else self.sx.toList()
        dx = None if not self.dx else self.dx.toList()
        return [self.value, sx, dx]

    def __eq__(self, other):
        """
        Compare two trees
        :param other: a tree
        :return: True if trees are equal; False otherwise
        """
        return other != None and \
               type(self) == type(other) and \
               self.value == other.value and \
               self.sx == other.sx and \
               self.dx == other.dx

    def __repr__(self, level=0):
        """
        Print a tree with a given indentation level
        :param level: intentation level
        :return: a string-representation of the tree
        """
        indent = "|  " * level
        res = "{0}Node_{1}: {2.value}".format(indent, id(self), self)
        indent = "|  " * (level + 1)
        if self.sx:
            res += "\n{}".format(self.sx.__repr__(level + 1))
        else:
            res += "\n{}{}".format(indent, self.sx)
        if self.dx:
            res += "\n{}".format(self.dx.__repr__(level + 1))
        else:
            res += "\n{}{}".format(indent, self.dx)
        return res

    @classmethod
    def randomTree(cls, level):
        """
        Generate a random tree of at most N levels
        :param level: N, the maximum height of the tree
        :return: a tree of at most N levels
        """
        if random.randint(0,
                          100) < 10 or level < 0:  # in 10% of the cases, it is None
            return None
        V = random.randint(1, 1000000)
        sx = cls.randomTree(level - random.randint(1,
                                                   3))  # shorten the height of the left subtree by 1, 2 or 3
        dx = cls.randomTree(level - random.randint(1,
                                                   3))  # shorten the height of the right subtree by 1, 2 or 3
        return cls(V, sx, dx)

if __name__ == '__main__':
    a_list = [1, [2, None, None],
             [3, [4, None, None],
              [5, None, None],
              ],
             ]
    tree = BinaryTree.fromList(a_list)
    tree2 = copy.deepcopy(tree)
    tree3 = BinaryTree.randomTree(10)

    print('A =', tree, sep='\n')
    print('B =', tree2, sep='\n')
    print('A =', tree.toList())
    print('C =', tree3)
    print('C =', tree3.toList())
