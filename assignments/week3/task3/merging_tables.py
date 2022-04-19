# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def get_parent(i):
    # use path compression heuristic
    if i != parent[i]:
        parent[i] = get_parent(parent[i])
    return parent[i]


def merge(i, j):
    # use union by rank heuristic
    i, j = get_parent(i), get_parent(j)

    if i == j:
        return

    global ans
    if rank[i] > rank[j]:
        parent[j] = i
        lines[i] += lines[j]
        lines[j] = 0
        ans = max(ans, lines[i])
    else:
        parent[i] = j
        lines[j] += lines[i]
        lines[i] = 0
        ans = max(ans, lines[j])

        if rank[i] == rank[j]:
            rank[j] += 1


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
