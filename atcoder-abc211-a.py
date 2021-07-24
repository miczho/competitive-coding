import sys

input = sys.stdin.readline 

def bp():
    a, b = map(int, input().split())
    print((a - b) / 3 + b)


if __name__ == '__main__':
    bp()