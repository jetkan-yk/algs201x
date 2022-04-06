# python3

from math import floor


def build_heap(n, data):
    swap_count = 0
    swap_list = []
    size = n - 1
    for i in range(floor(n/2), -1, -1):
        swap_count, swap_list, data = sift_down(i, size, data, swap_count, swap_list)
    return swap_count, swap_list
        
        
def sift_down(i, size, data, swap_count, swap_list):
    minIndex = i
    l = LeftChild(i + 1)
    if l <= size and data[l] < data[minIndex]:
        minIndex = l
    r = RightChild(i + 1)
    if r <= size and data[r] < data[minIndex]:
        minIndex = r
    if i != minIndex:
        data[i], data[minIndex] = data[minIndex], data[i]
        swap_count += 1
        swap_list.append((i, minIndex))
        swap_count, swap_list, data = sift_down(minIndex, size, data, swap_count, swap_list)
    return swap_count, swap_list, data
  
def LeftChild(i):
    return 2 * i - 1
 
def RightChild(i):
    return 2 * i

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swap_count, swap_list = build_heap(n, data)
    
    print(swap_count)
    for swap in swap_list:
        print(swap[0], swap[1])


if __name__ == "__main__":
    main()
