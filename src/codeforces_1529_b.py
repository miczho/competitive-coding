import sys

input = sys.stdin.readline 

def strangeSubsequences(n, arr):
    arr.sort()

    diff = float('inf')
    i = 0
    while i < n and arr[i] <= 0:
        if i != 0:
            diff = min(diff, abs(arr[i] - arr[i-1]))
        i += 1

    if i < n and diff >= arr[i]:
        i += 1

    return i


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]

        print(strangeSubsequences(n, arr))


if __name__ == '__main__':
    main()