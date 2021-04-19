import sys

input = sys.stdin.readline

def gcd(a, b):
    while b != 0: a, b = b, a%b
    return a


def prodOneModN(n):
    ans = set((i for i in range(1, n)))
    total = 1
    for i in range(2, n):
        if gcd(i, n) != 1:
            ans.remove(i)
        else:
            total *= i
            total %= n

    if total != 1:
        ans.remove(total)
    return [[len(ans)], sorted(list(ans))]


def main():
    n = int(input())
    ans = prodOneModN(n)
    for arr in ans:
        print(*arr)


if __name__ == '__main__':
    main()