import sys

input = sys.stdin.readline

def antiKnap(n, k):
    ans = set(i for i in range(1, n+1))
    ans.remove(k)
    start = k//2
    if not k%2:
        start -= 1
    for i in range(start, 0, -1):
        ans.remove(i)
    print(len(ans))
    print(*ans)


def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        antiKnap(n, k)


if __name__ == '__main__':
    main()