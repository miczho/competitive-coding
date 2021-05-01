import sys
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def signOfFriendship(n, d, h, arr):
    ans = 0.0
    for d2, h2 in arr:
        ans = max(ans, (d2*h - d*h2) / (d2 - d))
    return ans


def main():
    n, d, h = map(int, input().split())
    arr = [[int(i) for i in input().split()] for _ in range(n)]
    print(signOfFriendship(n, d, h, arr))


if __name__ == '__main__':
    main()