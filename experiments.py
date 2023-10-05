import alg
from typing import List, Tuple, Dict
from collections import Counter
import time
from functools import wraps
import array


class Heap:
    #мини
    def __init__(self):
        self.heaplist = [0, 0, 0]
        self.heapsize = -1
        self.maxsize = 3

    def _parent(self, i):
        return (i-1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self,i):
        return 2 * i + 2

    def _getmin(self):
        return self.heaplist[0]

    def build_heap(self, arr):
        self.heaplist = arr
        self.heapsize = len(arr) - 1
        self.maxsize = self.heapsize
        for i in range(self.heapsize // 2, -1, -1):
            self.siftdown(i)

    def siftup(self, i):
        while i > 0 and self.heaplist[self._parent(i)] > self.heaplist[i]:
            self.heaplist[self._parent(i)], self.heaplist[i] = self.heaplist[i], self.heaplist[self._parent(i)]
            print(self._parent(i), i)
            i = self._parent(i)

    def siftdown(self, i):
        l, r = self._left_child(i), self._right_child(i)
        min_i = i
        if l <= self.heapsize and self.heaplist[l] < self.heaplist[min_i]:
            min_i = l
        if r <= self.heapsize and self.heaplist[r] < self.heaplist[min_i]:
            min_i = r
        if i != min_i:
            self.heaplist[min_i], self.heaplist[i] = self.heaplist[i], self.heaplist[min_i]
            self.siftdown(min_i)

    def insert(self, p):
        if self.heapsize + 1 == self.maxsize:
            self.heaplist.extend(list(0 for _ in range(self.maxsize)))
            self.maxsize *= 2
        self.heapsize += 1
        self.heaplist[self.heapsize] = p
        self.siftup(self.heapsize)

    def extract_min(self):
        res = self._getmin()
        self.heaplist[0] = self.heaplist[self.heapsize]
        self.heapsize -= 1
        self.siftdown(0)
        return res

    def remove(self, i):
        self.heaplist[i] = self._getmin() + 1
        self.siftup(i)
        self.extract_min()

    def change_priority(self, i, p):
        oldp = self.heaplist[i]
        self.heaplist[i] = p
        if p > oldp: self.siftup(i)
        else: self.siftdown(i)

    def print(self):
        print(self.heaplist[:self.heapsize + 1])

if __name__ == "__main__":
    my_heap = Heap()
    l = [5, 4, 3, 2, 1]

    #for i in l:
    #    my_heap.insert(i)
    #my_heap.print()

    my_heap.build_heap(l)
    my_heap.print()
