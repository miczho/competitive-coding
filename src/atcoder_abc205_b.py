import sys

input = sys.stdin.readline 

def permCheck(n, arr):
    arr.sort()

    for i in range(n):
        if arr[i] != i+1:
            return 'No'
    return 'Yes'

def main():
    n = int(input())
    arr = [int(i) for i in input().split()]

    print(permCheck(n, arr))


if __name__ == '__main__':
    main()