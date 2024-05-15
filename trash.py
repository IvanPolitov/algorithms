import sys
sys.setrecursionlimit(50000)


class Node:
    def __init__(self, val, prev=None):
        self.val = val
        self.prev = prev
        self.sons = []


def tr(n, t):
    if n == 1:
        return 1
    tree = [Node(x) for x in range(n)]
    for i in range(n):
        if t[i] != -1:
            tree[t[i]].sons.append(tree[i])
            tree[i].prev = tree[t[i]]
        else:
            flag = i

    q = find_h(tree[flag])
    return q


def find_h(node):
    h = 1
    for c in node.sons:
        h = max(h, 1 + find_h(c))
    return h


print(tr(10 ** 6, [i+1 for i in range(10 ** 6-1)] + [-1]))
