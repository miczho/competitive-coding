'''
#segtree
'''

import sys

input = sys.stdin.readline 

segtree_n = 1
# usually this amt of nodes is enough
while segtree_n < 10 ** 5:
    segtree_n *= 2
segtree = [0] * 2 * segtree_n

def set(i, v, x=0, lx=0, rx=segtree_n):
    # reached the bottom
    if rx - lx == 1:
        segtree[x] = v;
        return

    m = (lx + rx) // 2
    if i < m:
        set(i, v, 2*x+1, lx, m)
    else:
        set(i, v, 2*x+2, m, rx)

    # operation changes based off needs
    segtree[x] = segtree[2*x+1] + segtree[2*x+2]


def get(l, r, x=0, lx=0, rx=segtree_n):
    # range is out of bounds
    if l >= rx or r <= lx: return 0
    # range is in bounds
    if l <= lx and r >= rx: return segtree[x]

    # range is partially in bounds
    m = (lx + rx) // 2
    a = get(l, r, 2*x+1, lx, m)
    b = get(l, r, 2*x+2, m, rx)

    # again, operation changes
    return a + b


def main():
    n, m = map(int, input().split())

    for i, v in enumerate(input().split()):
        set(i, int(v))

    for i in range(m):
        arr = [int(v) for v in input().split()]
        if arr[0] == 1:
            set(arr[1], arr[2])
        else:
            print(get(arr[1], arr[2]))


if __name__ == '__main__':
    main()