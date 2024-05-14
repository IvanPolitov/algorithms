class CircularLinkedList():
    _head = None
    _tail = None

    class Node:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev

        def __str__(self):
            return str(self.value)

    def __init__(self, node=None):
        if node is not None:
            _node = self.Node(node)
            self._head = _node
            self._tail = _node

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def is_empty(self):
        return self._head is None

    def __str__(self):
        if self.is_empty():
            return "None"
        else:
            _node = self._head
            output = '<-> (' + str(_node) + ") <-> "
            if _node.next is self._head:
                return output
            _node = _node.next
            while _node is not self._head:
                output += '(' + str(_node) + ") <-> "
                _node = _node.next
        return output[:-1]

    def insert(self, value):
        node = self.Node(value)
        if self.is_empty():
            self._head = node
            self._tail = node
            self._head.next = self._tail
            self._head.prev = self._tail
            self._tail.next = self._head
            self._tail.prev = self._head
        else:
            node.next = self._head
            node.prev = self._tail
            self._head.prev = node
            self._tail.next = node
            self._tail = node

    def pop(self):
        if self.is_empty():
            return None
        else:
            _node = self._head
            self._head = self._head.next
            self._head.prev = self._tail
            self._tail.next = self._head
            value = _node.value
            del _node
            return value


if __name__ == '__main__':
    q = CircularLinkedList()
    q.insert(1)
    q.insert(2)
    print(q)
    q.insert(3)
    print(q)
    q.insert(4)
    print(q)
    q.pop()
    print(q)
    q.pop()
    print(q)
