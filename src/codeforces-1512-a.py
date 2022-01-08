import sys
from collections import defaultdict

input = sys.stdin.readline

def spyDetect(n, arr):
    d = defaultdict(list)
    for i in range(n):
        d[arr[i]].append(i)

    for key in d:
        if len(d[key]) == 1:
            return d[key][0] + 1
    return -1


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        print(spyDetect(n, arr))


if __name__ == '__main__':
    main()