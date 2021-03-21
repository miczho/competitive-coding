import sys

input = sys.stdin.readline

def kGoodnessStr(n, k, s):
    diff = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            diff += 1
    return abs(k - diff)

def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        s = input()
        print(f'Case #{t+1}: {kGoodnessStr(n, k, s)}')

if __name__ == '__main__':
    main()