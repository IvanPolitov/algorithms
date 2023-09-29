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


my_dll = DoubleLinkedList()
for i in range(10):
    my_dll.push_back(i)
my_dll.print()
my_dll.remove_first()
my_dll.print()
my_dll.remove_last()
my_dll.print()
my_dll.remove_val(3)
my_dll.print()