# UCSanDiegoX ALGS201x - Data Structures Fundamentals

## ‼️ WARNING ‼️

This repository contains solutions to the UCSanDiegoX ALGS201x programming assignments. If you intend to take this course in the future, please read the plaigarism policy of the course before viewing this repository.

## 📖 Table of Contents

| Week | Task | Topic                   | Problem Statement                                         | Source Code                                              |
| ---- | ---- | ----------------------- | --------------------------------------------------------- | -------------------------------------------------------- |
| 1    | 1    | Stack, Bracket Matching | [Check brackets in the code](#check-brackets-in-the-code) | [check_brackets.py](assignments/week1/task1/check_brackets.py)       |
| 1    | 2    | Tree Travesal           | [Compute tree height](#compute-tree-height)               | [tree_height.py](assignments/week1/task2/tree_height.py) |

## 🔍 Problem Statements

### Check brackets in the code

In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the code.

Your friend is making a text editor for programmers. He is currently working on a feature that will find errors in the usage of different types of brackets. Code can contain any brackets from the set `[]{}()`, where the opening brackets are `[,{,` and `(` and the closing brackets corresponding to them are `],},` and `)`.

For convenience, the text editor should not only inform the user that there is an error in the usage of brackets, but also point to the exact place in the code with the problematic bracket. First priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it, like `]` in `]()`, or closes the wrong opening bracket, like `}` in `()[}`. If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like `(` in `{}([]`. If there are no mistakes, text editor should inform the user that the usage of brackets is correct.

part from the brackets, code can contain big and small latin letters, digits and punctuation marks.

More formally, all brackets in the code should be divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either one of them is nested inside another one as in `(foo[bar])` or they are separate as in `f(a,b)-g[c]`. The bracket `[` corresponds to the bracket `]`, `{` corresponds to `}`, and `(` corresponds to `)`.

### Compute tree height

Trees are used to manipulate hierarchical data such as hierarchy of categories of a retailer or the directory structure on your computer. They are also used in data analysis and machine learning both for hierarchical clustering and building complex predictive models, including some of the best-performing in practice algorithms like Gradient Boosting over Decision Trees and Random Forests. In the later modules of this course, we will introduce balanced binary search trees (BST) — a special kind of trees that allows to very efficiently store, manipulate and retrieve data. Balanced BSTs are thus used in databases for efficient storage and actually in virtually any non-trivial programs, typically via built-in data structures of the programming language at hand.

In this problem, your goal is to get used to trees. You will need to read a description of a tree from the input, implement the tree data structure, store the tree and compute its height.

You are given a description of a rooted tree. Your task is to compute and output its height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
