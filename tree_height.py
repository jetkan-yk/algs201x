# python3

import sys
import threading

class nodes:
    def __init__(self, parent, child=None):
        '''
        Initialize nodes
        '''
        self.parent = parent
        self.child = child
      
    def addChild(self, node):
        if self.child is None:
            self.child = []
        self.child.append(node)

def compute_height(n, parents):
    # Replace this code with a faster implementation
    '''
    max_height = 0
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
        max_height = max(max_height, height)
    return max_height
    '''
def maxDepth(node):
    if node.child is None:
        return 0
    children = node.child
    depth_list = []
    for child in children:
        depth_list.append(maxDepth(child))
    return max(depth_list, default=0) + 1
    
    

def main():
    # read input data
    n = int(input())
    parents = list(map(int, input().split()))
    
    #allocate nodes
    nodes_list = []
    for i in range(n):
        nodes_list.append(nodes(parents[i]))
    
    # read each parent index
    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes_list[parent_index].addChild(nodes_list[child_index])
    
    # return 0 if tree is empty
    if len(nodes_list) == 0:
        return 0
    
    # obtain height
    height = maxDepth(nodes_list[root]) + 1
    
    print(height)
    # success
    return 0

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
