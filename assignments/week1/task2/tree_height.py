# python3

import sys, threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, index):
        self.index = index
        self.children = list()

    def addChild(self, child):
        self.children.append(child)

    def __str__(self):
        children = ", ".join(map(str, self.children))
        return f"Node {self.index}: [{children}]"


class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parents = list(map(int, sys.stdin.readline().split()))

    def build_tree(self):
        self.nodes = [Node(i) for i in range(self.n)]

        for node in range(self.n):
            parent = self.parents[node]
            if parent == -1:
                self.root = node
            else:
                self.nodes[parent].addChild(node)

    def compute_height(self):
        # Replace this code with a faster implementation
        maxHeight = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parents[i]
            maxHeight = max(maxHeight, height)
        return maxHeight


def test():
    tree = Tree()
    tree.read()
    tree.build_tree()

    print(f"Root = {tree.root}")
    for node in tree.nodes:
        print(node)


def main():
    tree = Tree()
    tree.read()
    print(tree.compute_height())


# threading.Thread(target=main).start()
test()
