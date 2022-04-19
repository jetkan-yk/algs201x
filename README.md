# UCSanDiegoX ALGS201x - Data Structures Fundamentals

## ‼️ WARNING ‼️

This repository contains solutions to the UCSanDiegoX ALGS201x programming assignments. If you intend to take this course in the future, please read the plaigarism policy of the course before viewing this repository.

## 📖 Table of Contents

| Week | Task | Topic                           | Problem Statement                                                             | Source Code                                                        |
| ---- | ---- | ------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 1    | 1    | Stack, Bracket matching         | [Check brackets in the code](#check-brackets-in-the-code)                     | [check_brackets.py](assignments/week1/task1/check_brackets.py)     |
| 1    | 2    | DFS with stack                  | [Compute tree height](#compute-tree-height)                                   | [tree_height.py](assignments/week1/task2/tree_height.py)           |
| 1    | 3    | Single-process scheduler, Deque | [Network packet processing simulation](#network-packet-processing-simulation) | [process_packages.py](assignments/week1/task3/process_packages.py) |
| 3    | 1    | Heapify                         | [Convert array into heap](#convert-array-into-heap)                           | [build_heap.py](assignments/week3/task1/build_heap.py)             |
| 3    | 2    | Multi-process scheduler, Heapq  | [Parallel processing](#parallel-processing)                                   | [job_queue.py](assignments/week3/task2/job_queue.py)               |
| 3    | 3    | Union-Find Disjoint Set         | [Merging tables](#merging-tables)                                             | [merging_tables.py](assignments/week3/task3/merging_tables.py)     |
| 4    | 1    | Basic Dict                      | [Phone book](#phone-book)                                                     | [phone_book.py](assignments/week4/task1/phone_book.py)             |
| 4    | 2    | Hash chaining                   | [Hashing with chains](#hashing-with-chains)                                   | [hash_chains.py](assignments/week4/task2/hash_chains.py)           |
| 4    | 3    | Rabin-Karp, String hashing      | [Find pattern in text](#find-pattern-in-text)                                 | [hash_substring.py](assignments/week4/task3/hash_substring.py)     |
| 6    | 1    | Pre, In, Post order traversal   | [Binary tree traversals](#binary-tree-traversals)                             | [tree_orders.py](assignments/week6/task1/tree_orders.py)           |
| 6    | 2    | In-order traversal              | [Is it a BST](#is-is-a-binary-search-tree)                                    | [is_bst.py](assignments/week6/task2/is_bst.py)                     |
| 6    | 3    | BST recursion                   | [Is it a BST (hard)](#is-it-a-binary-search-tree-hard-version)                | [is_bst_hard.py](assignments/week6/task3/is_bst_hard.py)           |
| 6    | 4    |                                 | [Set with range sums](#set-with-range-sums)                                   | [set_range_sums.py](assignments/week6/task4/set_range_sum.py)      |
| 6    | 5    |                                 | [Rope](#rope)                                                                 | [rope.py](assignments/week6/task5/rope.py)                         |

## 🔍 Problem Statements

### Check brackets in the code

In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the code.

Your friend is making a text editor for programmers. He is currently working on a feature that will find errors in the usage of different types of brackets. Code can contain any brackets from the set `[]{}()`, where the opening brackets are `[,{,` and `(` and the closing brackets corresponding to them are `],},` and `)`.

For convenience, the text editor should not only inform the user that there is an error in the usage of brackets, but also point to the exact place in the code with the problematic bracket. First priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it, like `]` in `]()`, or closes the wrong opening bracket, like `}` in `()[}`. If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like `(` in `{}([]`. If there are no mistakes, text editor should inform the user that the usage of brackets is correct.

Apart from the brackets, code can contain big and small latin letters, digits and punctuation marks.

More formally, all brackets in the code should be divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either one of them is nested inside another one as in `(foo[bar])` or they are separate as in `f(a,b)-g[c]`. The bracket `[` corresponds to the bracket `]`, `{` corresponds to `}`, and `(` corresponds to `)`.

### Compute tree height

Trees are used to manipulate hierarchical data such as hierarchy of categories of a retailer or the directory structure on your computer. They are also used in data analysis and machine learning both for hierarchical clustering and building complex predictive models, including some of the best-performing in practice algorithms like Gradient Boosting over Decision Trees and Random Forests. In the later modules of this course, we will introduce balanced binary search trees (BST) — a special kind of trees that allows to very efficiently store, manipulate and retrieve data. Balanced BSTs are thus used in databases for efficient storage and actually in virtually any non-trivial programs, typically via built-in data structures of the programming language at hand.

In this problem, your goal is to get used to trees. You will need to read a description of a tree from the input, implement the tree data structure, store the tree and compute its height.

You are given a description of a rooted tree. Your task is to compute and output its height. Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.

### Network packet processing simulation

In this problem you will implement a program to simulate the processing of network packets.

You are given a series of incoming network packets, and your task is to simulate their processing. Packets arrive in some order. For each packet number $i$, you know the time when it arrived $A_i$ and the time it takes the processor to process it $P_i$ (both in milliseconds). There is only one processor, and it processes the incoming packets in the order of their arrival. If the processor started to process some packet, it doesn’t interrupt or stop until it finishes the processing of this packet, and the processing of packet $i$ takes exactly $P_i$ milliseconds.

The computer processing the packets has a network buffer of fixed size $S$. When packets arrive, they are stored in the buffer before being processed. However, if the buffer is full when a packet arrives (there are $S$ packets which have arrived before this packet, and the computer hasn’t finished processing any of them), it is dropped and won’t be processed at all. If several packets arrive at the same time, they are first all stored in the buffer (some of them may be dropped because of that — those which are described later in the input). The computer processes the packets in the order of their arrival, and it starts processing the next available packet from the buffer as soon as it finishes processing the previous one. If at some point the computer is not busy, and there are no packets in the buffer, the computer just waits for the next packet to arrive. Note that a packet leaves the buffer and frees the space in the buffer as soon as the computer finishes processing it.

### Convert array into heap

In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting algorithm called HeapSort. It has guaranteed worst-case running time of 𝑂($n$ log $n$) as opposed to QuickSort’s average running time of 𝑂($n$ log $n$). QuickSort is usually used in practice, because typically it is faster, but HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your computer.

The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the way, did you know that algorithms based on Heaps are widely used for external sort, when you need to sort huge files that don’t fit into memory of a computer?

Your task is to implement this first step and convert a given array of integers into a heap. You will do that by applying a certain number of swaps to the array. Swap is an operation which exchanges elements $a_i$ and $a_j$ of the array $a$ for some $i$ and $j$. You will need to convert the array into a heap using only 𝑂($n$) swaps, as was described in the lectures. Note that you will need to use a min-heap instead of a max-heap in this problem.

### Parallel processing

In this problem you will simulate a program that processes a list of jobs in parallel. Operating systems such as Linux, MacOS or Windows all have special programs in them called schedulers which do exactly this with the programs on your computer.

You have a program which is parallelized and uses $n$ independent threads to process the given list of $m$ jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the thread with smaller index takes the job. For each job you know exactly how long will it take any thread to process this job, and this time is the same for all the threads. You need to determine for each job which thread will process it and when will it start processing.

### Merging tables

In this problem, your goal is to simulate a sequence of merge operations with tables in a database.

There are $n$ tables stored in some database. The tables are numbered from 1 to $n$. All tables share the same set of columns. Each table contains either several rows with real data or a symbolic link to another table. Initially, all tables contain data, and $i$-th table has $r_i$ rows. You need to perform $m$ of the following operations:

1. Consider table number $\text{destination}_i$. Traverse the path of symbolic links to get to the data. That is,
   while $\text{destination}_i$ contains a symbolic link instead of real data do:
   $\text{destination}_i ← \texttt{symlink}(\text{destination}_i)$
2. Consider the table number $\text{source}_i$ and traverse the path of symbolic links from it in the same manner as for $\text{destination}_i$.
3. Now, $\text{destination}_i$ and $\text{source}_i$ are the numbers of two tables with real data. If $\text{destination}_i \neq \text{source}_i$, copy all the rows from table $\text{source}_i$ to table $\text{destination}_i$, then clear the table $\text{source}_i$ and instead of real data put a symbolic link to $\text{destination}_i$ into it.
4. Print the maximum size among all $n$ tables (recall that size is the number of rows in the table). If the table contains only a symbolic link, its size is considered to be 0.

### Phone book

In this problem you will implement a simple phone book manager.

In this task your goal is to implement a simple phone book manager. It should be able to process the following types of user’s queries:

- **add** number name. It means that the user adds a person with name name and phone number number to the phone book. If there exists a user with such number already, then your manager has to overwrite the corresponding name.
- **del** number. It means that the manager should erase a person with number number from the phone book. If there is no such person, then it should just ignore the query.
- **find** number. It means that the user looks for a person with phone number number. The manager should reply with the appropriate name, or with string `"not found"` (without quotes) if there is no such person in the book.

### Hashing with chains

In this problem you will implement a hash table using the chaining scheme. Chaining is one of the most popular ways of implementing hash tables in practice. The hash table you will implement can be used to implement a phone book on your phone or to store the password table of your computer or web service (but don’t forget to store hashes of passwords instead of the passwords themselves, or you will get hacked!).

In this task your goal is to implement a hash table with lists chaining. You are already given the
number of buckets 𝑚 and the hash function. It is a polynomial hash function where $S[i]$ is the ASCII code of the $i$-th symbol of $S$, $p$ = 1 000 000 007 and $x$ = 263. Your program should support the following kinds of queries:

- **add** string — insert string into the table. If there is already such string in the hash table, then just ignore the query.
- **del** string — remove string from the table. If there is no such string in the hash table, then just ignore the query.
- **find** string — output `"yes"` or `"no"` (without quotes) depending on whether the table contains string or not.
- **check** $i$ — output the content of the $i$-th list in the table. Use spaces to separate the elements of the list. If $i$-th list is empty, output a blank line.

When inserting a new string into a hash chain, you must insert it in the beginning of the chain.

### Find pattern in text

In this problem, your goal is to implement the Rabin–Karp’s algorithm for searching the given pattern in the given text.

### Binary tree traversals

In this problem you will implement in-order, pre-order and post-order traversals of a binary tree. These traversals were defined in the week 1 lecture on tree traversals, but it is very useful to practice implementing them to understand binary search trees better.

You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.

### Is is a binary search tree?

In this problem you are going to test whether a binary search tree data structure from some programming language library was implemented correctly. There is already a program that plays with this data structure by inserting, removing, searching integers in the data structure and outputs the state of the internal binary tree after each operation. Now you need to test whether the given binary tree is indeed a correct binary search tree. In other words, you want to ensure that you can search for integers in this binary tree using binary search through the tree, and you will always get correct result: if the integer is in the tree, you will find it, otherwise you will not.

You are given a binary tree with integers as its keys. You need to test whether it is a correct binary search tree. The definition of the binary search tree is the following: for any node of the tree, if its key is $x$, then for any node in its left subtree its key must be strictly less than $x$, and for any node in its right subtree its key must be strictly greater than $x$. In other words, smaller elements are to the left, and bigger elements are to the right. You need to check whether the given binary tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a tree, and each node has at most two children.

### Is it a binary search tree? Hard version

In this problem you are going to solve the same problem as the previous one, but for a more general case, when binary search tree may contain equal keys.

You are given a binary tree with integers as its keys. You need to test whether it is a correct binary search tree. Note that there can be duplicate integers in the tree, and this is allowed. The definition of the binary search tree in such case is the following: for any node of the tree, if its key is $x$, then for any node in its left subtree its key must be strictly less than $x$, and for any node in its right subtree its key must be greater than or equal to $x$. In other words, smaller elements are to the left, bigger elements are to the right, and duplicates are always to the right. You need to check whether the given binary tree structure satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a tree, and each node has at most two children.

### Set with range sums

In this problem, your goal is to implement a data structure to store a set of integers and quickly compute range sums.

Implement a data structure that stores a set $S$ of integers with the following allowed operations:

- **add**($i$) — add integer $i$ into the set $S$ (if it was there already, the set doesn’t change).
- **del**($i$) — remove integer $i$ from the set $S$ (if there was no such element, nothing happens).
- **find**($i$) — check whether $i$ is in the set $S$ or not.
- **sum**($l, r$)—output the sum of all elements $v$ in $S$ such that $l \leq v \leq r$.

### Rope

In this problem you will implement Rope — data structure that can store a string and efficiently cut a part (a substring) of this string and insert it in a different position. This data structure can be enhanced to become persistent — that is, to allow access to the previous versions of the string. These properties make it a suitable choice for storing the text in text editors.

You are given a string $S$ and you have to process $n$ queries. Each query is described by three integers $i, j, k$ and means to cut substring $S[i..j]$ ($i$ and $j$ are 0-based) from the string and then insert it after the $k$-th symbol of the remaining string (if the symbols are numbered from 1). If $k$ = 0, $S[i..j]$ is inserted in the beginning.
