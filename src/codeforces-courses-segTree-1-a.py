'''
#segmentTree
'''

import sys

input = sys.stdin.readline 

st_n = 1
# usually this amt of nodes is enough
while st_n < 10 ** 5:
    st_n *= 2
st = [0] * 2 * st_n

def set(i, v, x=0, lx=0, rx=st_n):
    # reached the bottom
    if rx - lx == 1:
        st[x] = v;
        return

    m = (lx + rx) // 2
    if i < m:
        set(i, v, 2*x+1, lx, m)
    else:
        set(i, v, 2*x+2, m, rx)

    # operation changes based off needs
    st[x] = st[2*x+1] + st[2*x+2]


def get(l, r, x=0, lx=0, rx=st_n):
    # range is out of bounds
    if l >= rx or r <= lx: return 0
    # range is in bounds
    if l <= lx and r >= rx: return st[x]

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