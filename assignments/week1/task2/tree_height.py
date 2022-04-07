# python3

import sys, threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, index):
        self.index = index
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        children = ", ".join(map(str, self.children))
        return f"Node {self.index}: [{children}]"


class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parents = list(map(int, sys.stdin.readline().split()))
        self._build_tree()

    def _build_tree(self):
        self.nodes = [Node(i) for i in range(self.n)]

        for node in range(self.n):
            parent = self.parents[node]
            if parent == -1:
                self.root = node
            else:
                self.nodes[parent].add_child(node)

    def compute_height(self):
        self.depths = [1] * self.n
        stack = [self.root]

        while stack:
            node = stack.pop()
            for child in self.nodes[node].children:
                self.depths[child] = self.depths[node] + 1
                stack.append(child)

        return max(self.depths)


def main():
    tree = Tree()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
