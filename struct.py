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

my_ll = LinkedList()
for i in range(10):
    my_ll.push_back(i)
my_ll.print()
my_ll.remove_last()
my_ll.print()
my_ll.remove_last()
my_ll.print()
my_ll.remove_last()
my_ll.print()
my_ll.remove_last()
my_ll.print()
www = my_ll.find_val(2)
print(www.next_node.value)
my_ll.remove_val(5)
my_ll.print()
