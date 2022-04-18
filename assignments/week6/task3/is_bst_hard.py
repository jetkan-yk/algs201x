#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

ROOT_NODE = 0
MAX_KEY = 2**32


def is_bst(tree):
    def check_range(node, min_key, max_key):
        if node == -1:
            return True

        key, left_child, right_child = tree[node]

        if key < min_key or key > max_key:
            return False

        return check_range(left_child, min_key, key - 1) and \
            check_range(right_child, key, max_key)

    if len(tree) < 2:
        return True

    return check_range(ROOT_NODE, -MAX_KEY, MAX_KEY)


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
