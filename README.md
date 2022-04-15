# UCSanDiegoX ALGS201x - Data Structures Fundamentals

## ‼️ WARNING ‼️

This repository contains solutions to the UCSanDiegoX ALGS201x programming assignments. If you intend to take this course in the future, please read the plaigarism policy of the course before viewing this repository.

## 📖 Table of Contents

| Week | Task | Topic                   | Problem Statement                                         | Source Code                                                    |
| ---- | ---- | ----------------------- | --------------------------------------------------------- | -------------------------------------------------------------- |
| 1    | 1    | Stack, Bracket matching | [Check brackets in the code](#check-brackets-in-the-code) | [check_brackets.py](assignments/week1/task1/check_brackets.py) |
| 1    | 2    | Tree travesal           | [Compute tree height](#compute-tree-height)               | [tree_height.py](assignments/week1/task2/tree_height.py)       |
| 3    | 1    | Heapify                 | [Convert array into heap](#convert-array-into-heap)       | [build_heap.py](assignments/week3/task1/build_heap.py)         |
| 3    | 2    | Heapq operations        | [Parallel processing](#parallel-processing)               | [job_queue.py](assignments/week3/task2/job_queue.py)           |
| 4    | 1    | Dict operations         | [Phone book](#phone-book)                                 | [phone_book.py](assignments/week4/task1/phone_book.py)         |
| 4    | 2    | Hash chaining           | [Hashing with chains](#hashing-with-chains)               | [hash_chains.py](assignments/week4/task2/hash_chains.py)       |
| 6    | 1    |                         | [Binary tree traversals](#binary-tree-traversals)         | [tree_orders.py](assignments/week6/task1/tree_orders.py)       |

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

### Convert array into heap

In this problem you will convert an array of integers into a heap. This is the crucial step of the sorting algorithm called HeapSort. It has guaranteed worst-case running time of 𝑂(𝑛 log 𝑛) as opposed to QuickSort’s average running time of 𝑂(𝑛 log 𝑛). QuickSort is usually used in practice, because typically it is faster, but HeapSort is used for external sort when you need to sort huge files that don’t fit into memory of your computer.

The first step of the HeapSort algorithm is to create a heap from the array you want to sort. By the way, did you know that algorithms based on Heaps are widely used for external sort, when you need to sort huge files that don’t fit into memory of a computer?

Your task is to implement this first step and convert a given array of integers into a heap. You will do that by applying a certain number of swaps to the array. Swap is an operation which exchanges elements 𝑎𝑖 and 𝑎𝑗 of the array 𝑎 for some 𝑖 and 𝑗. You will need to convert the array into a heap using only 𝑂(𝑛) swaps, as was described in the lectures. Note that you will need to use a min-heap instead of a max-heap in this problem.

### Parallel processing

In this problem you will simulate a program that processes a list of jobs in parallel. Operating systems such as Linux, MacOS or Windows all have special programs in them called schedulers which do exactly this with the programs on your computer.

You have a program which is parallelized and uses 𝑛 independent threads to process the given list of 𝑚 jobs. Threads take jobs in the order they are given in the input. If there is a free thread, it immediately takes the next job from the list. If a thread has started processing a job, it doesn’t interrupt or stop until it finishes processing the job. If several threads try to take jobs from the list simultaneously, the thread with smaller index takes the job. For each job you know exactly how long will it take any thread to process this job, and this time is the same for all the threads. You need to determine for each job which thread will process it and when will it start processing.

### Phone book

In this problem you will implement a simple phone book manager.

In this task your goal is to implement a simple phone book manager. It should be able to process the following types of user’s queries:

- **add** number name. It means that the user adds a person with name name and phone number number to the phone book. If there exists a user with such number already, then your manager has to overwrite the corresponding name.
- **del** number. It means that the manager should erase a person with number number from the phone book. If there is no such person, then it should just ignore the query.
- **find** number. It means that the user looks for a person with phone number number. The manager should reply with the appropriate name, or with string “not found" (without quotes) if there is no such person in the book.

### Hashing with chains

In this problem you will implement a hash table using the chaining scheme. Chaining is one of the most popular ways of implementing hash tables in practice. The hash table you will implement can be used to implement a phone book on your phone or to store the password table of your computer or web service (but don’t forget to store hashes of passwords instead of the passwords themselves, or you will get hacked!).

In this task your goal is to implement a hash table with lists chaining. You are already given the
number of buckets 𝑚 and the hash function. It is a polynomial hash function where 𝑆[𝑖] is the ASCII code of the 𝑖-th symbol of 𝑆, 𝑝 = 1 000 000 007 and 𝑥 = 263. Your program should support the following kinds of queries:

- **add** string — insert string into the table. If there is already such string in the hash table, then just ignore the query.
- **del** string — remove string from the table. If there is no such string in the hash table, then just ignore the query.
- **find** string — output “yes" or “no" (without quotes) depending on whether the table contains string or not.
- **check** 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of the list. If 𝑖-th list is empty, output a blank line.

When inserting a new string into a hash chain, you must insert it in the beginning of the chain.

### Binary tree traversals

In this problem you will implement in-order, pre-order and post-order traversals of a binary tree. These traversals were defined in the week 1 lecture on tree traversals, but it is very useful to practice implementing them to understand binary search trees better.

You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.
