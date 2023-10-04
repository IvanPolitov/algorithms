import alg
from typing import List, Tuple, Dict
from collections import Counter
import time
from functools import wraps
import array
class Heap:
    '''
    макси-куча
    мини-куча аналогично
    '''
    coll = []
    def __init__(self, coll):
        self.coll = coll
        self.size = len(coll)
        self.max_size = self.size * 2
        self.coll.extend(list(0 for _ in range(self.size)))
    def _parent(self, i):
        return (i-1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self,i):
        return 2 * i + 2

    def _sift_up(self, i):
        while i > 0 and self.coll[self._parent(i)] > self.coll[i]:
            self.coll[self._parent(i)], self.coll[i] = self.coll[i], self.coll[self._parent(i)]
            i = self._parent(i)

    def _sift_down(self, i):
        max_index = i
        l = self._left_child(i)
        if l <= self.size and self.coll[l] < self.coll[max_index]:
            max_index = l
        r = self._left_child(i)
        if r <= self.size and self.coll[r] < self.coll[max_index]:
            max_index = r
        if i != max_index:
            self.coll[i], self.coll[max_index] = self.coll[max_index], self.coll[i]
            self._sift_down(max_index)

    def insert(self, p):
        if self.size == self.max_size:
            self.max_size *= 2
            self.coll.extend(list(0 for _ in range(self.size)))
        self.size += 1
        self.coll[self.size] = p
        self._sift_up(self.size)

    def extract_max(self):
        res = self.coll[0]
        self.coll[0] = self.coll[self.size]
        self.size -= 1
        self._sift_down(0)
        return res

    def remove(self, i):
        self.coll[i] = self.get_max() + 1
        self._sift_up(i)
        self.extract_max()

    def get_max(self):
        return self.coll[0]

    def change_priority(self, i, p):
        old_p = self.coll[i]
        self.coll[i] = p
        if p > old_p: self._sift_up(i)
        else: self._sift_down(i)

    def print(self):
        print(self.coll[:self.size])

if __name__ == "__main__":
    my_heap = Heap([1, 2, 3, 4, 5])
    my_heap.print()
    my_heap.insert(8)
    my_heap.print()

