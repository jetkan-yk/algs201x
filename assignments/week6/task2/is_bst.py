#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

ROOT_NODE = 0


def is_bst(tree):
    def visit(node):
        if node == -1:
            return

        key, left_child, right_child = tree[node]

        visit(left_child)
        in_order.append(key)
        visit(right_child)

    def is_sorted(lst):
        for i in range(1, len(lst)):
            if lst[i - 1] > lst[i]:
                return False
        return True

    if len(tree) < 2:
        return True

    in_order = []
    visit(ROOT_NODE)
    return is_sorted(in_order)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_bst(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
