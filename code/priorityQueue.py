import unittest


class PQueue(object):
    """Priority Queue representation using a binary heap"""
    def __init__(self):
        self.arr = []

    def pop(self):
        mini = self.arr[0]  # the min is always the first item in the array
        self.arr[0] = self.arr.pop(-1)
        self._bubbledown()

    def push(self, x):
        self.arr.append(x)
        self._bubbleup()

    def _swap(self, i, j):
        temp = self.arr[i]
        self.arr[i] = self.arr[j]
        self.arr[j] = temp

    @staticmethod
    def _parent(x):
        return (x-1)/2

    def _bubbleup(self):
        index = len(self.arr)-1  # bubble up from the last position
        while index > 0 and self.arr[self._parent(index)] > self.arr[index]:
            # while not at the top and the parent is not the root.
            # swap
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def _minchild(self, index):
        left = 2*index+1
        right = 2*index+2
        if self.arr[right] > self.arr[left]:
            return left
        else:
            return right

    def _bubbledown(self):

        c = self._minchild(0)
        i = 0
        while c < len(self.arr) and self.arr[c] < self.arr[i]:
            self._swap(i, c)
            index = c
            c = self._minchild(c)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.Queue = PQueue()
        arr = [23, 35, 13, 34, 13, 5, 7, 12, 54]
        for a in arr:
            self.Queue.push(a)

    def test_min(self):
        self.assertEqual(min(self.Queue.arr), self.Queue.arr[0])

    def test_minAfterPop(self):
        self.Queue.pop()
        self.assertEqual(min(self.Queue.arr), self.Queue.arr[0])
        self.Queue.pop()
        self.Queue.pop()
        self.assertEqual(min(self.Queue.arr), self.Queue.arr[0])

    def test_minAfterPopPush(self):
        self.Queue.pop()
        self.Queue.push(0)
        self.assertEqual(min(self.Queue.arr), self.Queue.arr[0])

    def test_minAfterPopPushPop(self):
        pass

    def test_EnsureChildrenAlwaysGreaterThanParents(self):
        """test recurcisively :). It is a tree afterall"""


if __name__ == "__main__":
    unittest.main()
