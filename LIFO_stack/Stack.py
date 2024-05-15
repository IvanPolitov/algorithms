# Стек на односвязном списке
class Stack:
    _head = None

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)

    def __init__(self, node=None):
        if node is not None:
            _node = self.Node(node)
            self._head = _node

    def __str__(self):
        if self._head is None:
            return '[]'
        else:
            output = ''
            node = self._head
            while node is not None:
                output += str(node) + ' | '
                node = node.next
            output = output[:-2] + ']'
            return output

    def is_empty(self):
        return self._head is None

    def push(self, value):
        node = self.Node(value)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def pop(self):
        if self.is_empty():
            return None
        else:
            node = self._head
            value = node.value
            self._head = node.next
            del node
            return value

    def top(self):
        return self._head.value

    def __len__(self):
        if self.is_empty():
            return 0
        length = 0
        node = self._head
        while node is not None:
            length += 1
            node = node.next
        return length


if __name__ == '__main__':
    q = Stack()
    q.push(1)
    print(q)
    q.push(2)
    print(q)
    q.push(3)
    print(q.top())
    print(q.pop())
    print(len(q))
    # print(q)
    #
    # print(q)
    # print(q.pop())
    # print(q)
    # print(q.pop())
    # print(q)
