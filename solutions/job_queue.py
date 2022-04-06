# python3

from math import floor
from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

def build_heap(n, data):
    size = n - 1
    for i in range(floor(n/2), -1, -1):
        data = sift_down(i, size, data)
    return data

def compare_workers(worker1, worker2):
    if worker1[1] != worker2[1]:
        return worker1[1] < worker2[1]
    else:
        return worker1[0] < worker2[0]
   
def sift_down(i, size, data):
    minIndex = i
    l = LeftChild(i)
    if l <= size and compare_workers(data[l], data[minIndex]):
        minIndex = l
    r = RightChild(i)
    if r <= size and compare_workers(data[r], data[minIndex]):
        minIndex = r
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        data = sift_down(minIndex, size, data)
    return data
  
def LeftChild(i):
    return 2 * i + 1
 
def RightChild(i):
    return 2 * i + 2

def ChangePriority(i, p, data, size):
    oldp = data[i][1]
    data[i][1] = p
    if p > oldp:
        sift_down(i, size, data)
    elif p < oldp:
        # program is not intended to handle this case
        return -1
      
def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    
    workers = []
    for i in range(n_workers):
        tmp_list = [i, jobs[i]]
        workers.append(tmp_list)
        print(i, 0)
    
    build_heap(n_workers, workers)
    
    for i in range(n_workers, n_jobs):
        index = workers[0][0]
        started_at = workers[0][1]
        ChangePriority(0, started_at + jobs[i], workers, n_workers - 1)
        print(index, started_at)

if __name__ == "__main__":
    main()
