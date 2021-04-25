import sys
import random
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Soln():
    def __init__(self, n, arr):
        self.n = n
        self.arr = arr
        self.d = {}
        for i in range(n):
            self.d.setdefault(arr[i], list()).append(i)

    def bin(self, pick, val):
        num_freq = self.d[pick]
        
        l, r = -1, len(num_freq)
        while r > l + 1:
            m = (l + r) // 2
            if num_freq[m] <= val:
                l = m
            else:
                r = m

        return l

    def cutAndStick(self, l, r):
        max_freq = (r - l + 2) // 2
        picks = []
        for _ in range(25):
            i = random.randint(l, r)
            picks.append(self.arr[i])

        for p in picks:
            lower = self.bin(p, l-1)
            upper = self.bin(p, r)
            if upper - lower > max_freq:
                return str(2 * (upper - lower) - (r - l + 1))

        return '1'


def main():
    n, q = map(int, input().split())
    arr = [int(i) for i in input().split()]
    s = Soln(n, arr)
    ans = []
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1; r -= 1
        ans.append(s.cutAndStick(l, r))
    print('\n'.join(ans))


if __name__ == '__main__':
    main()