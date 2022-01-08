import sys, heapq

input = sys.stdin.readline 

def phoenixAndTowers(n, m, x, arr):
    towers, ans = list(), list()
    hi = 0

    for i in range(m, 0, -1):
       heapq.heappush(towers, (0, i))

    for i in arr:
        lo = heapq.heappop(towers)
        heapq.heappush(towers, (lo[0] + i, lo[1]))
        ans.append(lo[1])
        if lo[0] + i > hi:
            hi = lo[0] + i

    diff = hi - heapq.heappop(towers)[0]
    if diff > x:
        print('NO')
    else:
        print('YES')
        print(*ans)


def main():
    for t in range(int(input())):
        n, m, x = map(int, input().split())
        arr = [int(i) for i in input().split()]

        phoenixAndTowers(n, m, x, arr)


if __name__ == '__main__':
    main()