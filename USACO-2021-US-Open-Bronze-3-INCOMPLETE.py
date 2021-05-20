import sys

input = sys.stdin.readline 

imove = [-1, 0, 0, 1]
jmove = [0, -1, 1, 0]

class Soln():
    def __init__(self, n, m, arr):
        self.n = n
        self.m = m
        self.arr = arr

    def existsCow(self, x, y):
        if x >= 0 and y >= 0 and x < self.n and y < self.m and self.arr[x][y] == 'C':
            return True
        return False

    def acowdemiaIII(self):
        friends = set()
        ans = 0

        for i in range(self.n):
            for j in range(self.m):
                if self.arr[i][j] == 'G':
                    cows = list()
                    for k in range(4):
                        ii = i + imove[k]
                        jj = j + jmove[k]
                        if self.existsCow(ii, jj):
                            cows.append((ii, jj))
                    if len(cows) > 2:
                        ans += 1
                    elif len(cows) == 2:
                        cows.sort()
                        friends.add(tuple(cows))

        return len(friends) + ans


def main():
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    s = Soln(n, m, arr)
    print(s.acowdemiaIII())


if __name__ == '__main__':
    main()