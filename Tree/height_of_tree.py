import unittest


def height_of_tree(n: int, nodes: list) -> int:
    '''Список родителей'''
    max_length = 0
    for i in range(n):
        length = 1
        node = nodes[i]
        while node != -1:
            length += 1
            node = nodes[node]
        if length > max_length:
            max_length = length

    return max_length


class TestHeightOfTree(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, height_of_tree(
            10, [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]))

    def test2(self):
        self.assertEqual(3, height_of_tree(
            5, [4, -1, 4, 1, 1]))

    def test3(self):
        self.assertEqual(4, height_of_tree(
            5, [-1, 0, 4, 0, 3]))

    def test4(self):
        self.assertEqual(1, height_of_tree(
            1, [-1]))


if __name__ == '__main__':
    unittest.main()
