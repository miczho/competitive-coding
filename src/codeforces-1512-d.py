import sys

input = sys.stdin.readline

def corruptArr(n, b):
    b.sort()
    totals = {b[-1], b[-2]}

    t = sum(b[:-1])
    if (t - b[-2]) in totals: return b[:-2]
    for i in range(n):
        if (t - b[i]) == b[-1]: return b[:i] + b[i+1:-1]
    return -1


def main():
    for t in range(int(input())):
        n = int(input())
        b = [int(i) for i in input().strip().split()]
        ans = corruptArr(n, b)
        if type(ans) == list:
            print(*ans)
        else:
            print(ans)


if __name__ == '__main__':
    main()