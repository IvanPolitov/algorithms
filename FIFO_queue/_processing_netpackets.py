import unittest
from Queue import Queue


def process_netpacket(size, n, packets):
    q = Queue()
    time = 0
    times = []
    times_end = []
    packets = [(x.split()) for x in packets]
    packets = [(int(x[0]), int(x[1])) for x in packets]

    for packet in packets:
        if q.is_empty():
            times.append(packet[0])
            q.enqueue(packet)
            time = packet[0] + packet[1]
            times_end.append(time)
        elif packet[0] <= time:
            if size > len(q):
                times.append(time)
                q.enqueue(packet)
                time += packet[1]
                times_end.append(time)
            else:
                if packet[0] >= times_end[0]:
                    times_end.pop(0)
                    q.dequeue()
                    times.append(time)
                    q.enqueue(packet)
                    time += packet[1]
                    times_end.append(time)
                else:
                    times.append(-1)
        else:
            time = packet[0]
            times_end.pop(0)
            q.dequeue()
            q.enqueue(packet)
            times.append(time)
            time += packet[1]
            times_end.append(time)

    return times


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual([], process_netpacket(1, 0, []))

    def test2(self):
        self.assertEqual([0, 0, 0, 1, 1, 1, 2, -1], process_netpacket(
            2, 8, ['0 0', '0 0', '0 0', '1 0', '1 0', '1 1', '1 2', '1 3']))

    def test3(self):
        self.assertEqual([999999, 1000000, 1000000, - 1, - 1], process_netpacket(
            1, 5, ['999999 1', '1000000 0', '1000000 1', '1000000 0', '1000000 0']))

    def test4(self):
        self.assertEqual([2, 11, -1, 19, 21], process_netpacket(
            2, 5, ['2 9', '4 8', '10 9', '15 2', '19 1']))


if __name__ == '__main__':
    unittest.main()
    print(*process_netpacket(
        2, 8, ['0 0', '0 0', '0 0', '1 0', '1 0', '1 1', '1 2', '1 3']))
