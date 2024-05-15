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
    ml = [Node(x) for x in range(n)]
    for i in range(n):
        if t[i] != -1:
            ml[t[i]].sons.append(ml[i])
            ml[i].prev = ml[t[i]]
        else:
            flag = i

    q = find_h(ml[flag])
    return q


def find_h(node):
    h = 1
    for c in node.sons:
        h = max(h, 1 + find_h(c))
    return h


print(tr(10 ** 6, [i+1 for i in range(10 ** 6-1)] + [-1]))
