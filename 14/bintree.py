
import copy
import random

class BinTree:
    def __init__(self, V, sx=None, dx=None):
        self.value = V
        self.sx = sx
        self.dx = dx


################### FROM HERE ARE ONLY FUNCTIONS NEEDED FOR TESTING #####################

################### ATTENTION IT IS FORBIDDEN TO USE THE FUNCTIONS BELOW ###########################

    @classmethod
    def fromList(cls, lista):
        """
        Build the tree from a list [value, left, right].
        Where left and right are other trees or the None value
        :param lista:
        :return:
        """
        value, sx, dx = lista
        if sx: sx = cls.fromList(sx)
        if dx: dx = cls.fromList(dx)
        return cls(value, sx, dx)

    def toList(self):
        """
        Convert tree to list list [value, left, right].
        :return:
        """
        sx = None if not self.sx else self.sx.toList()
        dx = None if not self.dx else self.dx.toList()
        return [self.value, sx, dx]

    def __eq__(self, other):
        """
        Compare two trees
        :param other:
        :return:
        """
        return other != None and \
               type(self) == type(other) and \
               self.value == other.value and \
               self.sx == other.sx and \
               self.dx == other.dx

    def __repr__(self, livello=0):
        """
        Print a tree with a given indentation level
        :param livello: indentazione
        :return:
        """
        indent = "|  "*livello
        res = "{0}Nodo_{1}: {2.value}".format(indent, id(self), self)
        indent = "|  "*(livello+1)
        if self.sx:
            res += "\n{}".format(self.sx.__repr__(livello+1))
        else:
            res += "\n{}{}".format(indent, self.sx)
        if self.dx:
            res += "\n{}".format(self.dx.__repr__(livello+1))
        else:
            res += "\n{}{}".format(indent, self.dx)
        return res

    @classmethod
    def randomTree(cls, level):
        """
        Generate a random tree of at most level levels
        :param level:
        :return:
        """
        if random.randint(0, 100) < 10 or level < 0:    # nel 10% dei casi è None
            return None
        V = random.randint(1, 1000000)
        sx = cls.randomTree(level - random.randint(1,3)) # accorcio la profondita da 1 a 3 livelli a caso
        dx = cls.randomTree(level - random.randint(1,3)) # accorcio la profondita da 1 a 3 livelli a caso
        return cls(V, sx, dx)

if __name__ == '__main__':
    lista = [1, [2, None, None],
                [3, [4, None, None],
                    [5, None, None],
                ],
            ]
    albero  = BinTree.fromList(lista)
    albero2 = copy.deepcopy(albero)
    albero3 = BinTree.randomTree(10)

    print('A =', albero, sep='\n')
    print('B =', albero2, sep='\n')
    print('A =', albero.toList())
    print('C =', albero3 )
    print('C =', albero3.toList() )
