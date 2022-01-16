import sys

input = sys.stdin.readline 

segtree_n = 1
while segtree_n < 10 ** 5:
    segtree_n *= 2
segtree = [[float('inf'), 0] for _ in range(2 * segtree_n)]

def set(i, v, x=0, lx=0, rx=segtree_n):
    if rx - lx == 1:
        segtree[x][0] = v
        segtree[x][1] = 1
        return

    m = (lx + rx) // 2
    if i < m:
        set(i, v, 2*x+1, lx, m)
    else:
        set(i, v, 2*x+2, m, rx)

    if segtree[2*x+1][0] < segtree[2*x+2][0]:
        segtree[x][0] = segtree[2*x+1][0]
        segtree[x][1] = segtree[2*x+1][1]
    elif segtree[2*x+2][0] < segtree[2*x+1][0]:
        segtree[x][0] = segtree[2*x+2][0]
        segtree[x][1] = segtree[2*x+2][1]
    else:
        segtree[x][0] = segtree[2*x+1][0]
        segtree[x][1] = segtree[2*x+1][1] + segtree[2*x+2][1]


def get(l, r, x=0, lx=0, rx=segtree_n):
    if l >= rx or r <= lx: return (float('inf'), 0)
    if l <= lx and r >= rx: return segtree[x]

    m = (lx + rx) // 2
    a = get(l, r, 2*x+1, lx, m)
    b = get(l, r, 2*x+2, m, rx)

    if a[0] != b[0]:
        return a if a[0] < b[0] else b
    return (a[0], a[1] + b[1])


def main():
    n, m = map(int, input().split())

    for i, v in enumerate(input().split()):
        set(i, int(v))

    for _ in range(m):
        arr = [int(v) for v in input().split()]
        if arr[0] == 1:
            set(arr[1], arr[2])
        else:
            print(*get(arr[1], arr[2]))


if __name__ == '__main__':
    main()