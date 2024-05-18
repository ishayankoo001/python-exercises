import tree

def ex6(string_set):
   '''Design a function ex6(string_set) such that:
   - it is recursive or uses recursive function(s)/methods(s)









   - it receives a set of strings 'string_set' as argument
   - it exploits the strings in 'string_set' to reconstruct a binary
     tree in which the values of the nodes are single characters
   - it returns the reconstructed binary tree as a tree of nodes of
     type BinaryTree, defined in the attached tree.py library.
   Each string of 'string_set' represents a sequence of the values of
   the nodes traversed following the path from a leaf to the root of a
   binary tree. The tree is such that:
   - the value of each node is one single character
   - each internal node is locally ordered from left to right, namely:
     - each left child has a value smaller than that of the father
     - each right child has a value greater than that of the father

   Example: if the tree to reconstruct is

                     i     
                     |
             |-----------------|               
             h                 m 
             |                 |   
         |--------|        |------|   
         c        j        k      p
         |        |               |
      |-----|  |-----|         |-----|
      a     f  g     k         m     q    

   The set of strings is:
      { 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' }

   WARNING: it's FORBIDDEN to use any method defined in the class tree.py
   '''
   string_set = (sorted(string_set, key = lambda x:-len(x)))
   string_set = ["".join(reversed(x)) for x in string_set]
   tr = tree.BinaryTree(string_set[0][0])
   string_set = [x[1:] for x in string_set]
   for i in string_set:
      treeBuilder(tr,i)

   return tr

def treeBuilder(tr, string):
   if string == "":
      return tr
   i = string[0]
   if i<tr.value:
      if(tr.left != None and tr.left.value==i):
         return treeBuilder(tr.left, string[1:])
      tr.left = tree.BinaryTree(i)
      return treeBuilder(tr.left, string[1:])
   if i>tr.value:
      if(tr.right != None and tr.right.value==i):
         return treeBuilder(tr.right, string[1:])

      tr.right = tree.BinaryTree(i)
      return treeBuilder(tr.right, string[1:])



a = ex6({ 'achi', 'qpmi', 'gjhi', 'fchi', 'mpmi', 'kmi', 'kjhi' })
e = ['i',    ['h',   ['c',   ['a', None, None], ['f', None, None]], ['j',   ['g', None, None], [
            'k', None, None]]], ['m',   ['k',   None, None], ['p',   ['m', None, None], ['q', None, None]]]]
print(a)

l = tree.BinaryTree.toList(a)
print(l==e)
