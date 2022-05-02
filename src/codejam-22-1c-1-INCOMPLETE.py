import sys

input = sys.stdin.readline 

def letterBlocks(n, arr):
    left = {}
    right = {}
    full = {}
    vis = [0] * n
    res = []

    def isFull(s):
        m = len(s)
        for i in range(1, m):
            if s[i] != s[i-1]:
                return False
        return True

    def dfs(i, s):
        if s[0] in full:
            for x in full[s[0]]:
                res.append(x[1])
                vis[x[0]] = 1
        res.append(s)
        vis[i] = 1
        if s[-1] in full:
            for x in full[s[-1]]:
                res.append(x[1])
                vis[x[0]] = 1
        if s[-1] in left:
            return dfs(left[s[-1]][0], left[s[-1]][1])

    for i, s in enumerate(arr):
        if isFull(s):
            if s[0] not in full:
                full[s[0]] = []
            full[s[0]].append((i, s))
        else:
            l, r = s[0], s[-1]
            if l in left or r in right:
                return 'IMPOSSIBLE'
            left[l] = (i, s)
            right[r] = (i, s)
    # print(left)
    # print(right)
    # print(full)

    for i, s in enumerate(arr):
        if not isFull(s) and s[0] not in right:
            dfs(i, s)
    for i, s in enumerate(arr):
        if vis[i] == 0:
            res.append(s)

    res = ''.join(res)
    letters = set(res[0])
    for i in range(1, len(res)):
        if res[i] not in letters:
            letters.add(res[i])
        elif res[i-1] != res[i]:
            return 'IMPOSSIBLE'

    return res


def main():
    for t in range(int(input())):
        n = int(input())
        arr = input().split()
        print(f'Case #{t+1}: {letterBlocks(n, arr)}')


if __name__ == '__main__':
    main()