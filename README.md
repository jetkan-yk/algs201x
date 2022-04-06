# UCSanDiegoX ALGS201x - Data Structures Fundamentals

## ‼️ WARNING ‼️

This repository contains solutions to the UCSanDiegoX ALGS201x programming assignments. If you intend to take this course in the future, please read the plaigarism policy of the course before viewing this repository.

## 📖 Table of Contents

| Week | Task | Topic                 | Problem Statement                                         | Source Code                                        |
| ---- | ---- | --------------------- | --------------------------------------------------------- | -------------------------------------------------- |
| 1    | 1    | Basic Data Structures | [Check brackets in the code](#check-brackets-in-the-code) | [brackets.py](assignments/week1/task1/brackets.py) |

## 🔍 Problem Statements

### Check brackets in the code

#### Problem Introduction

In this problem you will implement a feature for a text editor to find errors in the usage of brackets in the code.

#### Problem Description

**Task.** Your friend is making a text editor for programmers. He is currently working on a feature that will find errors in the usage of different types of brackets. Code can contain any brackets from the set `[]{}()`, where the opening brackets are `[,{,` and `(` and the closing brackets corresponding to them are `],},` and `)`.

For convenience, the text editor should not only inform the user that there is an error in the usage of brackets, but also point to the exact place in the code with the problematic bracket. First priority is to find the first unmatched closing bracket which either doesn’t have an opening bracket before it, like `]` in `]()`, or closes the wrong opening bracket, like `}` in `()[}`. If there are no such mistakes, then it should find the first unmatched opening bracket without the corresponding closing bracket after it, like `(` in `{}([]`. If there are no mistakes, text editor should inform the user that the usage of brackets is correct.

part from the brackets, code can contain big and small latin letters, digits and punctuation marks.

More formally, all brackets in the code should be divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing bracket, and for any two pairs of brackets either one of them is nested inside another one as in `(foo[bar])` or they are separate as in `f(a,b)-g[c]`. The bracket `[` corresponds to the bracket `]`, `{` corresponds to `}`, and `(` corresponds to `)`.

**Input Format.** Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation marks and brackets from the set `[]{}()`.

**Constraints.** The length of 𝑆 is at least 1 and at most $10^{5}$.

**Output Format.** If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes). Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket.
