import sys

input = sys.stdin.readline 

def smallerStrs(n, k, s):
    MOD = 10 ** 9 + 7
    ans = 0
    power = [1]
    for i in range(n):
        power.append((k * power[i]) % (MOD))

    def lt(word):
        res = 0
        m = len(word)

        for i in range(m):
            res += (ord(word[i]) - ord('a')) * power[m - i - 1]
            res %= MOD

        return res

    for i in range(n//2 - 1, -1, -1):
        if s[i] > s[n-i-1]:
            return lt(s[:(n+1)//2]) 
        elif s[i] < s[n-i-1]:
            return (lt(s[:(n+1)//2]) + 1) % MOD
    return lt(s[:(n+1)//2]) 


def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = input()

        print(f'Case #{t+1}: {smallerStrs(n, k, s)}')


if __name__ == '__main__':
    main()