from sys import stdin


class StackMax:
    _head = None
    _max = None

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
        node_max = self.Node(value)
        if self.is_empty():
            self._head = node
            self._max = node
        else:
            node.next = self._head
            self._head = node
            if self._max.value < node_max.value:
                node_max.next = self._max
                self._max = node_max
            else:
                node_max = self.Node(self._max.value)
                node_max.next = self._max
                self._max = node_max

    def pop(self):
        if self.is_empty():
            return None
        else:
            node = self._head
            value = node.value
            self._head = node.next
            del node

            node_max = self._max
            self._max = node_max.next
            del node_max

            return value

    def top(self):
        if self.is_empty():
            return None
        return self._head.value

    def max(self):
        if self.is_empty():
            return None
        return self._max.value

    def __len__(self):
        if self.is_empty():
            return 0
        length = 0
        node = self._head
        while node is not None:
            length += 1
            node = node.next
        return length


def main(n, commands):
    q = StackMax()
    output = []
    commands_dict = {
        'push': q.push,
        'pop': q.pop,
        'max': q.max,
    }
    for command in commands:
        c = command.split()
        if c[0] == 'push':
            commands_dict[c[0]](int(c[1]))
        elif c[0] == 'pop':
            commands_dict[c[0]]()
        else:
            output.append(commands_dict[c[0]]())
    return output


if __name__ == '__main__':
    n = int(input())
    commands = [x.strip() for x in stdin.readlines()]
    print(*main(n, commands), sep='\n')
