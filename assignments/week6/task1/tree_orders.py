# python3

import sys, threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    ROOT_NODE = 0

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = []
        self.left = []
        self.right = []

        for _ in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key.append(a)
            self.left.append(b)
            self.right.append(c)

    def in_order(self):
        def visit(node):
            if node == -1:
                return
            visit(self.left[node])
            result.append(self.key[node])
            visit(self.right[node])

        result = []
        visit(TreeOrders.ROOT_NODE)
        return result

    def pre_order(self):
        def visit(node):
            if node == -1:
                return
            result.append(self.key[node])
            visit(self.left[node])
            visit(self.right[node])

        result = []
        visit(TreeOrders.ROOT_NODE)
        return result

    def post_order(self):
        def visit(node):
            if node == -1:
                return
            visit(self.left[node])
            visit(self.right[node])
            result.append(self.key[node])

        result = []
        visit(TreeOrders.ROOT_NODE)
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


threading.Thread(target=main).start()
