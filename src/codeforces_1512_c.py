import sys

input = sys.stdin.readline

def ABpalindrome(a, b, s):
    d, n = {'0':a, '1':b}, a + b

    if n == 1:
        if a == 1: return 0 if (s[0] == '0' or s[0] == '?') else -1
        if b == 1: return 1 if (s[0] == '1' or s[0] == '?') else -1
    if a%2 and b%2: return -1
    elif a%2:
        if s[n//2] == '?':
            s[n//2] = '0'
        elif s[n//2] == '1': return -1
        d['0'] -= 1
    elif b%2:
        if s[n//2] == '?':
            s[n//2] = '1'
        elif s[n//2] == '0': return -1
        d['1'] -= 1

    for i in range(n//2):
        if s[i] == s[n - i - 1]:
            if s[i] != '?': d[s[i]] -= 2
        elif s[i] == '?' or s[n - i - 1] == '?':
            if s[i] == '?':
                s[i] = s[n - i - 1]
                d[s[n - i - 1]] -= 2
            elif s[n - i - 1] == '?':
                s[n - i - 1] = s[i]
                d[s[i]] -= 2
        else: return -1

    for i in range(n//2):
        if s[i] == '?':
            if d['0'] > 1:
                s[i], s[n - i - 1] = '0', '0'
                d['0'] -= 2
            elif d['1'] > 1:
                s[i], s[n - i - 1] = '1', '1'
                d['1'] -= 2
            else: return -1

    if d['0'] != 0 or d['1'] != 0: return -1
    return ''.join(s)


def main():
    for t in range(int(input())):
        a, b = map(int, input().split())
        s = [ch for ch in input().strip()]
        print(ABpalindrome(a, b, s))


if __name__ == '__main__':
    main()