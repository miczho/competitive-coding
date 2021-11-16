import sys

def transformStr(s, f):
    ans = 0

    for a in s:
        tmp1 = 26
        for b in f:
            tmp2 = max(ord(a), ord(b)) - min(ord(a), ord(b))
            if tmp2 > 13:
                tmp2 = 26 - tmp2
            tmp1 = min(tmp1, tmp2)
        ans += tmp1

    return ans

def main():
    for t in range(int(input())):
        s = input()
        f = input()
        print(f'Case #{t+1}: {transformStr(s, f)}')

if __name__ == '__main__':
    main()
