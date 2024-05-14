class DoubleLinkedList:
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

    def __str__(self) -> str:
        if self.is_empty():
            return "None"
        else:
            _node = self._head
            output = ""
            while _node is not None:
                output += '(' + str(_node) + ") <-> "
                _node = _node.next
        return output[:-5]

    def is_empty(self):
        return self._head is None

    def push_tail(self, value):
        node = self.Node(value)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

    def push_head(self, value):
        node = self.Node(value)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._head.prev = node
            node.next = self._head
            self._head = node

    def pop_tail(self):
        if self.is_empty():
            return None
        if self._head is self._tail:
            node = self._head
            value = node.value
            self._head = self._tail = None
            del node
            return value
        else:
            node = self._tail
            value = node.value
            self._tail = self._tail.prev
            self._tail.next = None
            del node
            return value

    def pop_head(self):
        if self.is_empty():
            return None
        if self._head is self._tail:
            node = self._head
            value = node.value
            self._head = self._tail = None
            del node
            return value
        else:
            node = self._head
            value = node.value
            self._head = self._head.next
            self._head.prev = None
            del node
            return value


if __name__ == "__main__":
    q = DoubleLinkedList()
    print(q)
    q.push_tail(1)
    q.push_tail(2)
    q.push_tail(3)
    q.push_head(0)
    print(q)
    print(q.head)
    print(q.tail)
    print(q.pop_tail())
    print(q)
    print(q.pop_head())
    print(q)
