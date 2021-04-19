import sys, math

input = sys.stdin.readline

def perfectImperfectArr(n, arr):
    for i in arr:
        if math.sqrt(i) % 1:
            return 'YES'
    return 'NO'


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        print(perfectImperfectArr(n, arr))


if __name__ == '__main__':
    main()