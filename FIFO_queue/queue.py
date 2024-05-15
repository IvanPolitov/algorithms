# Очередь на односвязном списке
class Queue:
    _head = None
    _tail = None
    _length = 0

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None

        def __str__(self):
            return str(self.value)

    def __init__(self, node=None):
        if node is not None:
            _node = self.Node(node)
            self._head = _node

    def __str__(self) -> str:
        if self.is_empty():
            return "None"
        else:
            _node = self._head
            output = ""
            while _node is not None:
                output += '(' + str(_node) + ") -> "
                _node = _node.next
        return output[:-4]

    def __len__(self) -> int:
        return self._length

    def is_empty(self):
        return self._head is None

    def enqueue(self, value):
        _node = self.Node(value)
        self._length += 1
        if self.is_empty():
            self._head = _node
            self._tail = _node
        else:
            self._tail.next = _node
            self._tail = _node

    def dequeue(self):
        if self.is_empty():
            return None
        self._length -= 1
        _node = self._head
        value = _node.value
        self._head = self._head.next
        del _node
        return value

    def top(self):
        if self.is_empty():
            return None
        return self._head.value


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(len(q))
    q.dequeue()
    print(q)
    print(q.dequeue())
    q.enqueue(4)
    print(q)
    q.dequeue()
    print(q)
    print(q.is_empty())
