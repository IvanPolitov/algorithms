import unittest


class MinHeap:
    def __init__(self, a=None):
        self.couples = []
        if a is not None:
            self.heap = a
            self.size = len(a)
            self.build_heap()
        else:
            self.heap = []
            self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return i * 2 + 1

    def right(self, i):
        return i * 2 + 2

    def insert(self, value):
        self.size += 1
        self.heap.append(value)
        self.sift_up(self.size - 1)

    def extract_min(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.sift_down(0)
        self.size -= 1
        return result

    def sift_up(self, i):
        if i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            self.sift_up(self.parent(i))

    def sift_down(self, i):
        min_index = i
        left, right = self.left(i), self.right(i)

        if left < self.size and self.heap[left] < self.heap[i]:
            min_index = left

        if right < self.size and self.heap[right] < self.heap[i]:
            min_index = right

        if min_index != i:
            self.heap[min_index], self.heap[i] = self.heap[i], self.heap[min_index]
            self.couples.append((self.heap[i], self.heap[min_index]))
            self.sift_down(min_index)

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)


def change_number(n, arr):
    pass


class TestHeightOfTree(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, change_number(
            10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]))

    def test2(self):
        self.assertEqual(3, change_number(
            5, [4, -1, 4, 1, 1]))

    def test3(self):
        self.assertEqual(4, change_number(
            5, [-1, 0, 4, 0, 3]))

    def test4(self):
        self.assertEqual(1, change_number(
            1, [-1]))


if __name__ == '__main__':
    # unittest.main()
    c = [5, 4, 3, 2, 1]
    q = MinHeap(c)
    print(q.heap)
    print(q.couples)
    print(q.size)
