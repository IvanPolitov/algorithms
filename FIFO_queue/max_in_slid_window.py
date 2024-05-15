import unittest
from Queue import Queue


def max_in_slid_window(n, arr, m):
    q = Queue()


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
