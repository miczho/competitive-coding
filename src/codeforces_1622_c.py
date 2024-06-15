import sys

input = sys.stdin.readline 

def setOrDecrease(n, k, arr):
    psum = [0]
    
    def isValid(moves):
        for i in range(min(n, moves+1)):
            if (arr[0] - moves + i) * (i + 1) + psum[n - i] - psum[1] <= k:
                return True
        return False

    arr.sort()

    for x in arr:
        psum.append(psum[-1] + x)

    hi = max(0, arr[0] - int(k // n)) + n - 1
    lo = hi - n
    while lo != hi - 1:
        mid = int((lo + hi) // 2)
        if isValid(mid):
            hi = mid
        else:
            lo = mid

    return hi


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        arr = [int(x) for x in input().split()]
        print(setOrDecrease(n, k, arr))


if __name__ == '__main__':
    main()