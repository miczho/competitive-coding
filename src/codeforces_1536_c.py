import sys
from collections import defaultdict

input = sys.stdin.readline 

def gcd(a, b):
    while b != 0: a, b = b, a%b
    return a

def dilucAndKaeya(n, s):
    cnt = defaultdict(int)
    res = list()

    d, k = 0, 0
    for x in s:
        if x == 'D':
            d += 1
        else:
            k += 1
        tmp = gcd(d, k)
        cnt[(d // tmp, k // tmp)] += 1
        res.append(cnt[(d // tmp, k // tmp)])

    return res


def main():
    for t in range(int(input())):
        n = int(input())
        s = input().strip()

        print(*dilucAndKaeya(n, s))


if __name__ == '__main__':
    main()