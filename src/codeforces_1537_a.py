import sys

input = sys.stdin.readline 

def arithmeticArr(n, arr):
    total = sum(arr)

    if total / n == 1:
        return 0
    elif total / n < 1:
        return 1

    cnt = n
    while True:
        if total / cnt <= 1:
            return cnt - n
        cnt += 1


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]

        print(arithmeticArr(n, arr))


if __name__ == '__main__':
    main()