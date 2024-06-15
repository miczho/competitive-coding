import sys

input = sys.stdin.readline 

st_n = 1
while st_n < 10 ** 5:
    st_n *= 2
st = [[float('inf'), 0] for _ in range(2 * st_n)]

def set(i, v, x=0, lx=0, rx=st_n):
    if rx - lx == 1:
        st[x][0] = v
        st[x][1] = 1
        return

    m = (lx + rx) // 2
    if i < m:
        set(i, v, 2*x+1, lx, m)
    else:
        set(i, v, 2*x+2, m, rx)

    if st[2*x+1][0] < st[2*x+2][0]:
        st[x][0] = st[2*x+1][0]
        st[x][1] = st[2*x+1][1]
    elif st[2*x+2][0] < st[2*x+1][0]:
        st[x][0] = st[2*x+2][0]
        st[x][1] = st[2*x+2][1]
    else:
        st[x][0] = st[2*x+1][0]
        st[x][1] = st[2*x+1][1] + st[2*x+2][1]


def get(l, r, x=0, lx=0, rx=st_n):
    if l >= rx or r <= lx: return (float('inf'), 0)
    if l <= lx and r >= rx: return st[x]

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