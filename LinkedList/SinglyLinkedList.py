class SinglyLinkedList:
    _head = None
    _tail = None

    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self, node=None):
        if node is not None:
            _node = self.Node(node)
            self._head = _node
            self._tail = _node

    def __str__(self) -> str:
        if self.is_empty():
            return "None"
        else:
            _node = self._head
            output = ""
            while _node is not None:
                output += '(' + str(_node.value) + ") -> "
                _node = _node.next
        return output[:-4]

    def is_empty(self):
        return self._head is None

    def push_tail(self, value):
        node = self.Node(value)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node

    def push_head(self, value):
        node = self.Node(value)
        if self.is_empty():
            self._head = node
            self._tail = node
        else:
            node.next = self._head
            self._head = node

    def pop_tail(self):
        if self.is_empty():
            return None
        elif self._head == self._tail:
            _node = self._head
            value = _node.value
            self._head = self._tail = None
            del _node
            return value
        else:
            _node = self._head
            value = self._tail.value
            while _node.next is not self._tail:
                _node = _node.next
            del _node.next
            self._tail = _node
            _node.next = None
            return value

    def pop_head(self):
        if self.is_empty():
            return None
        elif self._head == self._tail:
            _node = self._head
            value = _node.value
            self._head = self._tail = None
            del _node
            return value
        else:
            _node = self._head
            value = _node.value
            self._head = _node.next
            del _node
            return value


if __name__ == "__main__":
    q = SinglyLinkedList()
    q.push_tail(1)
    q.push_tail(2)
    q.push_tail(3)
    print(q)
    print(q.pop_head())
    print(q.pop_tail())
    print(q)
