import sys
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, arr = None, None

def check(m):
    s = set()
    for a in arr:
        s.add(sum(1 << i for i in range(5) if a[i] >= m))
    
    for x in s:
        for y in s:
            for z in s:
                if(x | y | z == (1 << 5) - 1):
                    return True
    return False


def madTeam():
    l, r = 0, 10**9 + 1
    while r > l+1:
        m = (l + r) // 2
        if check(m):
            l = m
        else:
            r = m

    return l


def main():
    global n, arr
    n = int(input())
    arr = [[int(i) for i in input().split()] for _ in range(n)]
    print(madTeam())


if __name__ == '__main__':
    main()