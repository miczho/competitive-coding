import sys
from collections import deque

input = sys.stdin.readline 

def numOfShortestPaths(n, g):
    MOD = 10 ** 9 + 7
    dist = [None]*(n+1)
    cnt = [0]*(n+1)
    q = deque()

    dist[1] = 0; cnt[1] = 1
    q.append(1)
    while q:
        x = q.popleft()
        for i in g[x]:
            if dist[i] == None:
                dist[i] = dist[x] + 1
                cnt[i] = cnt[x]
                q.append(i)
            elif dist[i] == dist[x] + 1:
                cnt[i] += cnt[x]
                cnt[i] %= MOD

    print(cnt[n])


def main():
    n, m = map(int, input().split())

    g = [list() for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    numOfShortestPaths(n, g)


if __name__ == '__main__':
    main()