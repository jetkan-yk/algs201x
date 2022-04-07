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
        for node in self.nodes:
            parent = self.parents[node.index]
            if parent == -1:
                self.root = self.nodes[node.index]
            else:
                self.nodes[parent].add_child(node.index)

    def _max_height(self, node: Node):
        if not node.children:
            return 1
        return 1 + max([self._max_height(self.nodes[child]) for child in node.children])

    def compute_height(self):
        return self._max_height(self.root)


def main():
    tree = Tree()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
