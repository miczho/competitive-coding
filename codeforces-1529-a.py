import sys

input = sys.stdin.readline 

def bigArrr(n, arr):
    arr.sort()

    m = arr[0]
    res = 0
    i = 0
    while i < n and arr[i] == m:
        res += 1
        i += 1

    return n - res


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]

        print(bigArrr(n, arr))


if __name__ == '__main__':
    main()