import bintree

def es14(tree, x, count=0):
  if(tree.dx != None):
    count = es14(tree.dx, x+1, count)
  if(tree.sx != None):
    count = es14(tree.sx, x+1, count)
  if((tree.value % x) == 0):
    count+=1
  return count
