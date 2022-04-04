# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
  def __init__(self, key, left, right):
    self.key = key
    self.left = left
    self.right = right

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.node = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.node[i] = Node(a, b, c)

  def inOrder(self):
    self.result = []
    inOrderTraversal(self.result, self.node[0], self.node)
    return self.result

  def preOrder(self):
    self.result = []
    preOrderTraversal(self.result, self.node[0], self.node)
    return self.result

  def postOrder(self):
    self.result = []
    postOrderTraversal(self.result, self.node[0], self.node)
    return self.result

def inOrderTraversal(result, N, node_list):
	if N.left == -1 and N.right == -1:
		result.append(N.key)
		return
	if N.left != -1:
		inOrderTraversal(result, node_list[N.left], node_list)
	result.append(N.key)
	if N.right != -1:
		inOrderTraversal(result, node_list[N.right], node_list)
      
def preOrderTraversal(result, N, node_list):
	if N.left == -1 and N.right == -1:
		result.append(N.key)
		return
	result.append(N.key)
	if N.left != -1:
		preOrderTraversal(result, node_list[N.left], node_list)
	if N.right != -1:
		preOrderTraversal(result, node_list[N.right], node_list)
      
def postOrderTraversal(result, N, node_list):
	if N.left == -1 and N.right == -1:
		result.append(N.key)
		return
	if N.left != -1:
		postOrderTraversal(result, node_list[N.left], node_list)
	if N.right != -1:
		postOrderTraversal(result, node_list[N.right], node_list)
	result.append(N.key)
    
def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
