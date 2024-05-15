# Очередь из двух стеков

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


class QueueTwoStacks:
    _input = None
    _output = None

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self._input = Stack()
        self._output = Stack()

    def __str__(self):
        return str(self._input) + r'\/' + str(self._output)

    def is_empty(self):
        return (self._input is None) and (self._output is None)

    def enqueue(self, value):
        _node = self.Node(value)
        self._input.push(_node)

    def dequeue(self):
        if self._output.is_empty():
            while not self._input.is_empty():
                self._output.push(self._input.pop())
        return self._output.pop()


if __name__ == '__main__':
    q = QueueTwoStacks()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    print(q)
    print(q.dequeue())
    print(q)

    q.enqueue(11)
    q.enqueue(12)
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
    print(q.dequeue())
    print(q)
