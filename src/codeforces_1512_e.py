"""
#incomplete
"""

import sys

input = sys.stdin.readline

def permBySum(n, l, r, s):
    nums = set((i for i in range(1, n+1)))
    used = set()
    x = r - l + 1
    tmp = 1
    while x > 1:
        s -= tmp
        nums.remove(tmp)
        used.add(tmp)
        tmp += 1
        x -= 1
    if s in tmp


def main():
    for t in range(int(input())):
        n, l, r, s = map(int, input().strip().split())
        ans = permBySum(n, l, r, s)
        if type(ans) == list:
            print(*ans)
        else:
            print(ans)


if __name__ == '__main__':
    main()