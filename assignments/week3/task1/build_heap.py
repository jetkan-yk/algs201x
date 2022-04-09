# python3


class HeapBuilder:
    def __init__(self):
        self._n = 0
        self._data = []
        self._swaps = []

    def read_data(self):
        self._n = int(input())
        self._data = [int(s) for s in input().split()]
        assert self._n == len(self._data)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def _siftdown(self, i):
        min_child = i

        left_child = 2 * i + 1
        if left_child < self._n and self._data[left_child] < self._data[min_child]:
            min_child = left_child

        right_child = 2 * i + 2
        if right_child < self._n and self._data[right_child] < self._data[min_child]:
            min_child = right_child

        if i != min_child:
            self._swap(i, min_child)
            self._siftdown(min_child)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._swaps.append((i, j))

    def heapify(self):
        for i in reversed(range(self._n // 2)):
            self._siftdown(i)

    def solve(self):
        self.read_data()
        self.heapify()
        self.write_response()


if __name__ == "__main__":
    heap_builder = HeapBuilder()
    heap_builder.solve()
