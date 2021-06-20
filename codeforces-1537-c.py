import sys

input = sys.stdin.readline 

def challengeCliffs(n, h):
    if n == 2: return sorted(h)

    h.sort()

    best = 0
    for i in range(n-1):
        if h[i+1] - h[i] < h[best+1] - h[best]:
            best = i

    return h[best+1:] + h[:best+1]


def main():
    for t in range(int(input())):
        n = int(input())
        h = [int(i) for i in input().split()]

        print(*challengeCliffs(n, h))


if __name__ == '__main__':
    main()