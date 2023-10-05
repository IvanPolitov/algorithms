#Односвязный список
class LinkedList:
    first = None
    last = None

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def is_empty(self):
        if self.first:
            return False
        else:
            return True

    def make_lonely_node(self, value):      #создает первую ноду в пустом списке. внутренняя функция
        self.first = self.Node(value)
        self.last = self.first

    def push_back(self, value):
        if self.is_empty():
            self.make_lonely_node(value)
            return

        new_node = self.Node(value)
        self.last.next_node = new_node
        self.last = new_node

    def push_forward(self, value):
        if self.is_empty():
            self.make_lonely_node(value)
            return

        new_node = self.Node(value)
        new_node.next_node = self.first
        self.first = new_node

    def remove_first(self):
        if self.is_empty():
            return
        if self.first == self.last:
            del self.first
            self.first = self.last = None
            return
        node = self.first
        self.first = self.first.next_node
        del node

    def remove_last(self):
        if self.is_empty():
            return
        if self.first == self.last:
            self.first = self.last = None
            return
        node = self.first
        while node.next_node != self.last:
            node = node.next_node
        del self.last
        self.last = node
        self.last.next_node = None

    def find_val(self, val):
        if self.is_empty():
            return
        node = self.first
        while node.value != val:
            node = node.next_node
        return node

    def remove_val(self, val):
        if self.is_empty():
            return
        if val == self.first.value:
            self.remove_first()
            return
        if val == self.first.value:
            self.remove_first()
            return
        node = self.first

        while node.next_node.value != val:
            node = node.next_node
        temp = node.next_node
        del temp
        node.next_node = node.next_node.next_node

    def print(self):
        if self.is_empty():
            print(None)
        else:
            i = self.first
            while i:
                print(i.value, end=' ')
                i = i.next_node
            print()

class DoubleLinkedList:
    first = None
    last = None

    class Node:
        def __init__(self, value, next_node=None, prev_node=None):
            self.value = value
            self.next_node = next_node
            self.prev_node = prev_node

    def is_empty(self):
        if self.first:
            return False
        else:
            return True

    def make_lonely_node(self, value):      #создает первую ноду в пустом списке. внутренняя функция
        self.first = self.Node(value)
        self.last = self.first

    def push_back(self, value):
        if self.is_empty():
            self.make_lonely_node(value)
            return

        new_node = self.Node(value)
        self.last.next_node = new_node
        new_node.prev_node = self.last
        self.last = new_node

    def push_forward(self, value):
        if self.is_empty():
            self.make_lonely_node(value)
            return

        new_node = self.Node(value)
        new_node.next_node = self.first
        self.first.prev_node = new_node
        self.first = new_node

    def remove_first(self):
        if self.is_empty():
            return
        if self.first == self.last:
            del self.first
            self.first = self.last = None
            return
        node = self.first
        self.first = self.first.next_node
        self.first.prev_node = None
        del node

    def remove_last(self):
        if self.is_empty():
            return
        if self.first == self.last:
            del self.first
            self.first = self.last = None
            return
        node = self.first
        self.last = self.last.prev_node
        self.last.next_node = None
        del node

    def find_val(self, val):
        if self.is_empty():
            return
        node = self.first
        while node.value != val:
            node = node.next_node
        return node

    def remove_val(self, val):
        if self.is_empty():
            return
        if val == self.first.value:
            self.remove_first()
            return
        if val == self.first.value:
            self.remove_first()
            return
        node = self.first
        while node.next_node.value != val:
            node = node.next_node
        temp = node.next_node
        del temp
        node.next_node = node.next_node.next_node
        node.next_node.prev_node = node

    def print(self):
        if self.is_empty():
            print(None)
        else:
            i = self.first
            while i:
                print(i.value, end=' ')
                i = i.next_node
            print()

class Stack:
    #на односвязном списке
    def __init__(self, sup_min=False, sup_max=False):
        self.first = None
        self.min = None
        self.max = None
        self.sup_min = sup_min
        self.sup_max = sup_max

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def is_empty(self):
        if self.first:
            return False
        else:
            return True

    def push(self, val):
        if self.is_empty():
            self.first = self.Node(val)

            if self.sup_min:
                self.min = self.Node(val)
            if self.sup_max:
                self.max = self.Node(val)
            return

        new_node = self.Node(val, next_node=self.first)
        self.first = new_node

        if self.sup_min:
            if val < self.min.value:
                new_node = self.Node(val, next_node=self.min)
                self.min = new_node
            else:
                new_node = self.Node(self.min.value, next_node=self.min)
                self.min = new_node
        if self.sup_max:
            if val > self.max.value:
                new_node = self.Node(val, next_node=self.max)
                self.max = new_node
            else:
                new_node = self.Node(self.max.value, next_node=self.max)
                self.max = new_node

    def pop(self):
        if self.is_empty():
            return
        temp = self.first
        self.first = self.first.next_node
        if self.sup_min:
            temp_min = self.min
            self.min = self.min.next_node
            del temp_min
        if self.sup_max:
            temp_max = self.max
            self.max = self.max.next_node
            del temp_max
        return temp.value

    def top(self):
        if self.is_empty():
            return
        return self.first.value

    def get_min(self):
        if self.is_empty():
            return
        return self.min.value

    def get_max(self):
        if self.is_empty():
            return
        return self.max.value

    def len(self):
        if self.is_empty():
            return 0
        else:
            i = self.first
            l = 0
            while i:
                l += 1
                i = i.next_node
            return l

    def print(self):
        if self.is_empty():
            print(None)
        else:
            i = self.first
            while i:
                print(i.value, end=' ')
                i = i.next_node
            print()

class Queue:
    #на односвязном списке
    def __init__(self):
        self.front = None
        self.back = None

    class Node:
        def __init__(self, value, next_node=None):
            self.value = value
            self.next_node = next_node

    def is_empty(self):
        if self.front:
            return False
        else:
            return True

    def enqueue(self, val):
        if self.is_empty():
            self.front = self.Node(val)
            self.back = self.front
            return
        new_node = self.Node(val)
        self.back.next_node = new_node
        self.back = new_node

    def dequeue(self):
        if self.is_empty():
            return
        temp = self.front
        self.front = self.front.next_node
        return temp.value

    def len(self):
        if self.is_empty():
            return 0
        else:
            i = self.front
            l = 0
            while i:
                l += 1
                i = i.next_node
            return l

    def print(self):
        if self.is_empty():
            print(None)
        else:
            i = self.front
            while i:
                print(i.value, end=' ')
                i = i.next_node
            print()

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

my_stack = Queue()
my_stack.print()
for i in range(10):
    my_stack.enqueue(i)
my_stack.print()

my_stack.enqueue(-1)
my_stack.enqueue(28)
my_stack.enqueue(3)
my_stack.print()
my_stack.dequeue()
my_stack.print()
my_stack.dequeue()
my_stack.dequeue()
my_stack.print()
my_stack.dequeue()
print(my_stack.len())
my_stack.print()

