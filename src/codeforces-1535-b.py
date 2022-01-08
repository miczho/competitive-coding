import sys

input = sys.stdin.readline 

def gcd(a, b):
    while b != 0: a, b = b, a%b
    return a


def arrReodering(n, arr):
    res = 0
    odd = []; even = []
    for x in arr:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    arr = even + odd

    for i in range(n):
        for j in range(i+1, n):
            if i == j: continue
            if gcd(arr[i], 2 * arr[j]) != 1:
                res += 1

    return res


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]

        print(arrReodering(n, arr))


if __name__ == '__main__':
    main()