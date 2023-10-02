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

    def print(self):
        if self.is_empty():
            print(None)
        else:
            i = self.front
            while i:
                print(i.value, end=' ')
                i = i.next_node
            print()


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

my_stack.print()

