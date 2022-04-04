#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right
    
def IsBinarySearchTree(tree, nodes):
  result = []
  inOrderTraversal(result, tree[0], tree)
  for i in range(len(result) - 1):
    if result[i] > result[i + 1]:
      return False
  return True

def inOrderTraversal(result, N, tree):
  if N.left == -1 and N.right == -1:
    result.append(N.key)
    return result
  if N.left != -1 and N.left is not None:
    inOrderTraversal(result, tree[N.left], tree)
  result.append(N.key)
  if N.right != -1 and N.right is not None:
    inOrderTraversal(result, tree[N.right], tree)

def main():
  nodes = int(sys.stdin.readline().strip())
  if nodes <= 1:
    print("CORRECT")
    return 0
  tree = []
  for i in range(nodes):
    [a, b, c] = list(map(int, sys.stdin.readline().strip().split()))
    tree.append(Node(a, b, c))
  if IsBinarySearchTree(tree, nodes):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
