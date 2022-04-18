# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def get_parent(table):
    # find parent and compress path
    return parent[table]


def merge(destination, source):
    read_destination, real_source = get_parent(destination), get_parent(source)

    if read_destination == real_source:
        return False

    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size

    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)
