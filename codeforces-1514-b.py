import sys

input = sys.stdin.readline

def sumBig(n, k):
    return (n ** k) % 1_000_000_007


def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        print(sumBig(n, k))


if __name__ == '__main__':
    main()