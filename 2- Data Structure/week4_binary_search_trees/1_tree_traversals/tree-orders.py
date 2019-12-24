# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(input())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, input().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c


  def inOrder(self, ind):
      if self.left[ind] != -1 and self.right[ind] != -1:
          self.inOrder(self.left[ind])
          print(self.key[ind], end=" ")
          self.inOrder(self.right[ind])
          
      elif self.left[ind] != -1:
          self.inOrder(self.left[ind])
          print(self.key[ind], end=" ")
          
      elif self.right[ind] != -1:
          print(self.key[ind], end=" ")
          self.inOrder(self.right[ind])
          
      else:   
          print(self.key[ind], end=" ")
          
  def preOrder(self, ind):
      if self.left[ind] != -1 and self.right[ind] != -1:
          print(self.key[ind], end=" ")
          self.preOrder(self.left[ind])
          self.preOrder(self.right[ind])
          
      elif self.left[ind] != -1:
          print(self.key[ind], end=" ")
          self.preOrder(self.left[ind])
          
      elif self.right[ind] != -1:
          print(self.key[ind], end=" ")
          self.preOrder(self.right[ind])
      else:   
          print(self.key[ind], end=" ")
          
  def postOrder(self, ind):
      if self.left[ind] != -1 and self.right[ind] != -1:
          self.postOrder(self.left[ind])
          self.postOrder(self.right[ind])
          print(self.key[ind], end=" ")
      elif self.left[ind] != -1:
          self.postOrder(self.left[ind])
          print(self.key[ind], end=" ")          
      elif self.right[ind] != -1:
          self.postOrder(self.right[ind])
          print(self.key[ind], end=" ")
      else:   
          print(self.key[ind], end=" ")


def main():
    tree = TreeOrders()
    tree.read()
    tree.inOrder(0)
    print("")
    tree.preOrder(0)
    print("")
    tree.postOrder(0)

threading.Thread(target=main).start()
