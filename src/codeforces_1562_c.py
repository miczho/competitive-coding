import sys

input = sys.stdin.readline 

def rings(n, s):
    for i in range(n):
        if s[i] == '0':
            if i + 1 <= n // 2:
                return [i+1, n, i+2, n]
            return [1, i+1, 1, i]

    return [1, n-1, 2, n]


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        print(*rings(n, s))


if __name__ == '__main__':
    main()