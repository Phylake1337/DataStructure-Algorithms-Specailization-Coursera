#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def nodeCheck(tree, _range, ind, BST):
    nodeKey = tree[ind][0]
    leftInd = tree[ind][1]
    rightInd = tree[ind][2]
    
    if not(_range[0] <= nodeKey < _range[1]):
#        print("BST should be false")
#        print("the current range", _range, "the key", nodeKey)
        BST = False
        return BST
    
    rightNodeRange = (nodeKey, _range[1])
    leftNodeRange = (_range[0], nodeKey)
    
    if leftInd != -1 and rightInd != -1:
        return (nodeCheck(tree, leftNodeRange, leftInd, BST)
                and nodeCheck(tree, rightNodeRange, rightInd, BST))
        
    elif leftInd != -1:
        return nodeCheck(tree, leftNodeRange, leftInd, BST)
        
    elif rightInd != -1:
        return nodeCheck(tree, rightNodeRange, rightInd, BST)
    else:
        return BST
    
def IsBinarySearchTree(tree):
    BST = True
    BST = nodeCheck(tree, (-float("inf"), float("inf")), 0, BST)
    return BST



def main():
  nodes = int(input().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, input().strip().split())))
    
  if nodes == 0:
      print("CORRECT")
      return
  
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
