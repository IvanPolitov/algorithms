import unittest


class Tree:
    def __init__(self, value, parent=None):
        self.value = value
        self.height = 1
        self.parent: Tree = parent
        self.children: list[Tree] = []

    def __repr__(self):
        return str(self.value)


def h(tree: Tree):
    height = 1
    for x in tree.children:
        height = max(height, 1 + h(x))
    return height


def height_of_tree(n: int, nodes: list) -> int:
    '''Список родителей'''
    trees = []
    for i, c in enumerate(nodes):
        trees.append(Tree(i, c))
    flag = 0
    for tree in trees:
        if tree.parent != -1:
            trees[tree.parent].children.append(tree)
        else:
            flag = tree
    return h(flag)


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
