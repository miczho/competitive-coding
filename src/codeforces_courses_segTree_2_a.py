import sys

input = sys.stdin.readline 

st_n = 1
while st_n < 10 ** 5:
    st_n *= 2
st = [float('-inf')] * 2 * st_n

def set(i, v, x=0, x_l=0, x_r=st_n):
    if x_r - x_l == 1:
        st[x] = v
        return

    m = (x_l + x_r) // 2
    if i < m:
        set(i, v, 2*x+1, x_l, m)
    else:
        set(i, v, 2*x+2, m, x_r)

    st[x] = max(st[2*x+1], st[2*x+2], st[2*x+1] + st[2*x+2])


def get(l, r, x=0, x_l=0, x_r=st_n):
    if l >= x_r or r <= x_l: return float('-inf')
    if l <= x_l and r >= x_r: return st[x]

    m = (x_l + x_r) // 2
    a = get(l, r, 2*x+1, x_l, m)
    b = get(l, r, 2*x+2, m, x_r)

    return max(a, b, a + b)


def main():
    n, m = map(int, input().split())

    for i, v in enumerate(input().split()):
        set(i, int(v))

    print(get(0, n))
    for _ in range(m):
        arr = [int(v) for v in input().split()]
        set(arr[0], arr[1])
        print(get(0, n))


if __name__ == '__main__':
    main()