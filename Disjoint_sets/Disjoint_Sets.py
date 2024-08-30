'''
Считаем, что наши объекты - это просто числа
'''


class Disjoint_Sets:
    '''
    Реализация непересекающихся множеств в виде корневых деревьев.
    'parent[i] = j' означает, что элемент j является родителем элемента i.
    '''

    def __init__(self):
        '''
        Массив, в котором хранятся потомки и массив с рангом каждого поддерева
        '''
        self.parent = []
        self.rank = []

    def make_set(self, x):
        '''
        Создаем узел дерева: одноэлементное множество
        '''
        if x >= len(self.parent):
            while x >= len(self.parent):
                self.parent.append(-1)
                self.rank.append(-1)
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_id, y_id = self.find(x), self.find(y)

        if x_id == y_id:
            return

        if self.rank[x_id] > self.rank[y_id]:
            self.parent[y_id] = x_id
        else:
            self.parent[x_id] = y_id
            if self.rank[x_id] == self.rank[y_id]:
                self.rank[y_id] += 1


if __name__ == '__main__':
    q = Disjoint_Sets()
    q.make_set(1)
    q.make_set(2)
    q.make_set(3)
    q.make_set(4)
    q.make_set(5)
    q.make_set(6)
    print(q.parent)
    print(q.rank)

    q.union(2, 4)
    print()
    print(q.parent)
    print(q.rank)
    q.union(5, 2)
    print()
    print(q.parent)
    print(q.rank)
    q.union(3, 1)
    print()
    print(q.parent)
    print(q.rank)
    q.union(2, 3)
    print()
    print(q.parent)
    print(q.rank)
    q.union(2, 6)
    print()
    print(q.parent)
    print(q.rank)
