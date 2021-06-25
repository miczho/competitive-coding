import sys

input = sys.stdin.readline 

def pleasantPairs(n, arr):
    res = 0

    for j in range(1, n+1):
        if arr[j] >= 2*j: continue
        tmp = 1
        while (tmp * arr[j]) < (2 * j):
            i = tmp * arr[j] - j
            if i > 0 and arr[i] == tmp:
                res += 1
            tmp += 1

    return res


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [-1]
        for i in input().split():
            arr.append(int(i))

        print(pleasantPairs(n, arr))


if __name__ == '__main__':
    main()