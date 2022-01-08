import sys
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def ufoInvasion(s):
    n, target = len(s), 'ZONe'
    ans = 0
    for i in range(n-3):
        valid = True
        for j in range(4):
            if s[i+j] != target[j]:
                valid = False
                break
        if valid:
            ans += 1

    return ans


def main():
    s = str(input().strip())
    print(ufoInvasion(s))


if __name__ == '__main__':
    main()