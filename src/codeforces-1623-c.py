import sys

input = sys.stdin.readline 

def balancedStoneHeaps(n, arr):

    def isValid(target):
        arr2 = [0] * n

        for i in range(n-1, 1, -1):
            if arr[i] + arr2[i] < target:
                return False
            d = int((arr[i] + min(0, arr2[i] - target)) // 3)
            arr2[i-1] += d
            arr2[i-2] += 2 * d

        return arr[0] + arr2[0] >= target and arr[1] + arr2[1] >= target

    lo = 1
    hi = arr[n-1] + 1
    while lo != hi - 1:
        mid = int((lo + hi) // 2)
        if isValid(mid):
            lo = mid
        else:
            hi = mid

    return lo


def main():
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        print(balancedStoneHeaps(n, arr))


if __name__ == '__main__':
    main()