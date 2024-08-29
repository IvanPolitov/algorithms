import unittest
from Stack import Stack


def parentheses(s: str) -> int | str:
    par = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    q = Stack()
    for i, c in enumerate(s):
        if c in '([{':
            q.push((c, i))
        elif c in ')]}':
            if q.is_empty():
                return i + 1
            if par[c] == q.top()[0]:
                q.pop()
            else:
                return i + 1
    if q.is_empty():
        return 'Success'
    else:
        return q.top()[1] + 1


class TestParentheses(unittest.TestCase):
    def test1(self):
        self.assertEqual('Success', parentheses('([](){([])})'))

    def test2(self):
        self.assertEqual(1, parentheses('{'))

    def test3(self):
        self.assertEqual(7, parentheses('{{[()]]'))

    def test4(self):
        self.assertEqual(10, parentheses('foo(bar[i);'))

    def test5(self):
        self.assertEqual(3, parentheses('[]([]'))


if __name__ == '__main__':
    unittest.main()
