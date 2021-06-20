import sys

input = sys.stdin.readline 

def eraseExtendEasy(n, k, s):
    res = 'z' * k

    for i in range(1, n+1):
        word = (s[:i] * ((k+i-1) // i))[:k]
        if word < res:
            res = word

    return res


def main():
    n, k = map(int, input().split())
    s = input().strip()

    print(eraseExtendEasy(n, k, s))


if __name__ == '__main__':
    main()