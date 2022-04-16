# python3

import sys, threading

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
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
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return result

    def pre_order(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return result

    def post_order(self):
        result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


threading.Thread(target=main).start()
