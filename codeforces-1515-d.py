import sys

input = sys.stdin.readline 

def phoenixAndSocks(n, l, r, arr):
    left, right = [0]*n, [0]*n
    ans = 0

    for i in range(l):
        left[arr[i] - 1] += 1
    for i in range(l, n):
        right[arr[i] - 1] += 1

    if l < r:
        l, r = r, l
        left, right, = right, left

    for i in range(n):
        m = min(left[i], right[i])
        l -= m; r -= m
        left[i] -= m; right[i] -= m
        if l > r and left[i] != 0:
            m = min((l-r)//2, left[i]//2)
            l -= 2 * m
            left[i] -= 2 * m
            ans += m

    ans += ((l+r)//2) + ((l-r)//2)
    print(ans)


def main():
    for t in range(int(input())):
        n, l, r = map(int, input().split())
        arr = [int(i) for i in input().split()]

        phoenixAndSocks(n, l, r, arr)


if __name__ == '__main__':
    main()