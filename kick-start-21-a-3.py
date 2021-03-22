import sys, heapq

input = sys.stdin.readline

def rabbitHouse(r, c, arr):
    imov, jmov = [1, -1, 0, 0], [0, 0, 1, -1]
    vis, q, res = [[0]*c for _ in range(r)], [], 0
    
    for i in range(r):
        for j in range(c):
            heapq.heappush(q, (-arr[i][j], i, j))

    while q:
        val, i, j = heapq.heappop(q)
        if vis[i][j]: continue
        vis[i][j] = 1
        for z in range(4):
            ii = i + imov[z]
            jj = j + jmov[z]
            if ii >= 0 and ii < r and jj >= 0 and jj < c:
                if not vis[ii][jj]:
                    if (abs(arr[ii][jj] - arr[i][j]) > 1) and (arr[ii][jj] < arr[i][j]):
                            res += arr[i][j] - arr[ii][jj] - 1
                            arr[ii][jj] = arr[i][j] - 1
                            heapq.heappush(q, (-arr[ii][jj], ii, jj))
    return res


def main():
    for t in range(int(input())):
        r, c = map(int, input().split())
        arr = []
        for _ in range(r):
            arr.append([int(i) for i in input().split()])
        print(f'Case #{t+1}: {rabbitHouse(r, c, arr)}')


if __name__ == '__main__':
    main()