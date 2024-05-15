import unittest


class Stack:
    _head = None
    _length = 0

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
        self._length += 1
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def pop(self):
        if self.is_empty():
            return None
        else:
            self._length -= 1
            node = self._head
            value = node.value
            self._head = node.next
            del node
            return value

    def top(self):
        return self._head.value

    def __len__(self):
        return self._length


def max_in_slid_window(n, arr, m):
    _input = Stack()
    _output = Stack()
    max_list = []
    flag = False
    for i in arr:
        if len(_input) == m:
            while len(_input) > 0:
                node = _input.pop()[0]
                if _output.is_empty():
                    _output.push((node, node,))
                else:
                    _output.push((node, max(node, _output.top()[1]),))
            flag = True

        if flag:
            if not _input.is_empty():
                max_list.append(max(_input.top()[1], _output.pop()[1]))
            else:
                max_list.append(_output.pop()[1])

        if _input.is_empty():
            _input.push((i, i,))
        else:
            _input.push((i, max(i, _input.top()[1]),))

    while len(_input) > 0:
        node = _input.pop()[0]
        if _output.is_empty():
            _output.push((node, node,))
        else:
            _output.push((node, max(node, _output.top()[1]),))

    if len(_output) >= m:
        if len(_input) > 0:
            max_list.append(max(_input.top()[1], _output.pop()[1]))
        else:
            max_list.append(_output.pop()[1])

        # print(_input, '|||', _output)
    return max_list


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual([7, 7, 5, 6, 6], max_in_slid_window(
            8, [2, 7, 3, 1, 5, 2, 6, 2], 4))

    def test2(self):
        self.assertEqual([2, 1, 5], max_in_slid_window(
            3, [2, 1, 5], 1))

    def test3(self):
        self.assertEqual([9], max_in_slid_window(
            3, [2, 3, 9], 3))


if __name__ == "__main__":
    unittest.main()
    print(max_in_slid_window(
        8, [2, 7, 3, 1, 5, 2, 6, 2], 4))
