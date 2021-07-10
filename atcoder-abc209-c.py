import sys

input = sys.stdin.readline 

def main():
    MOD = 10**9+7
    n = int(input())
    c = [int(i) for i in input().split()]

    c.sort()
    if c[-1] < len(c):
        print(0)
    else:
        res = 1
        for i in range(len(c)):
            res *= c[i] - i
            res %= MOD
        print(res)


if __name__ == '__main__':
    main()