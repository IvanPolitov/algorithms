from Heap import Heap
import random


def build_heap_from_list(a: list):
    size = len(a)

    def sift_down(i):
        max_index = i
        left, right = 2 * i + 1, 2 * i + 2

        if left < size and a[left] > a[max_index]:
            max_index = left
        if right < size and a[right] > a[max_index]:
            max_index = right

        if max_index != i:
            a[max_index], a[i] = a[i], a[max_index]
            sift_down(max_index)

    for i in range(size // 2, -1, -1):
        sift_down(i)


def heap_sort(a: list) -> list:
    q = Heap()

    for i in a:
        q.insert(i)

    b = []
    for i in range(q.size):
        b.append(q.extract_max())

    return b


def heap_sort_inplace(a: list) -> list:
    build_heap_from_list(a)
    size = len(a) - 1

    def sift_down(i):
        max_index = i
        left, right = 2 * i + 1, 2 * i + 2

        if left <= size and a[left] > a[max_index]:
            max_index = left
        if right <= size and a[right] > a[max_index]:
            max_index = right

        if max_index != i:
            a[max_index], a[i] = a[i], a[max_index]
            sift_down(max_index)

    while size > 0:
        a[0], a[size] = a[size], a[0]
        size -= 1
        sift_down(0)
        print(f'{size:<3}: ', a)
    sift_down(0)


if __name__ == '__main__':
    a = [x for x in range(10)]
    b = [x for x in range(10)]
    c = [x for x in range(10)]

    random.shuffle(a)
    random.shuffle(b)
    print(heap_sort(a))
    print()
    print(b)
    heap_sort_inplace(b)
    print(b)
    print(c)

    q = [x for x in range(10)]
    h = Heap(q)
    print(h.heap)
