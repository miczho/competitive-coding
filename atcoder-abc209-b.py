import sys

input = sys.stdin.readline 

def main():
    n, x = map(int, input().split())
    arr = [int(i) for i in input().split()]

    for i, a in enumerate(arr):
        if i & 1 == 1:
            x -= a-1
        else:
            x -= a

    if x >= 0:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()