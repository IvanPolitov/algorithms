# Куча в списке. На массиве выглядело бы аналогично,
# но нам бы потребовалось завести переменную max_size,
# которая определяла бы размер массива, а также
# изменять размер массива по мере его заполнения.

class Heap:
    heap = []
    size = 0

    def __init__(self, a=None):
        if a is not None:
            self.heap = a
            self.size = len(a)
            self.build_heap()
        else:
            self.heap = []
            self.size = 0

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(
                i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i):
        max_index = i
        l = self.left_child(i)
        if l < self.size and self.heap[l] > self.heap[max_index]:
            max_index = l
        r = self.right_child(i)
        if r < self.size and self.heap[r] > self.heap[max_index]:
            max_index = r

        if max_index != i:
            self.heap[max_index], self.heap[i] = self.heap[i], self.heap[max_index]
            self.sift_down(max_index)

    def insert(self, value):
        self.size += 1
        self.heap.append(value)
        self.sift_up(self.size - 1)

    def extract_max(self):
        result = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.sift_down(0)
        self.size -= 1
        return result

    def remove(self, i):
        self.heap[i] = self.heap[0] + 1
        self.sift_up(i)
        self.extract_max()

    def change_priority(self, i, p):
        oldp = self.heap[i]
        self.heap[i] = p
        if p > oldp:
            self.sift_up(i)
        if p < oldp:
            self.sift_down(i)

    def get_max(self):
        return self.heap[0]

    def build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)



