#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

ROOT_NODE = 0


def is_bst(tree):
    def visit(node):
        if node == -1:
            return True

        key, left_child, right_child = tree[node]

        if left_child == right_child == -1:
            max_vals[node] = min_vals[node] = key
        elif visit(left_child) and visit(right_child):
            if left_child != -1 and max_vals[left_child] >= key:
                return False
            if right_child != -1 and min_vals[right_child] < key:
                return False

            min_vals[node] = min(key, min_vals[left_child])
            max_vals[node] = max(key, max_vals[right_child])
        else:
            return False
        return True

    if len(tree) < 2:
        return True

    max_vals = [None] * len(tree)
    min_vals = [None] * len(tree)
    return visit(ROOT_NODE)


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
