import sys

input = sys.stdin.readline 

def main():
    a, b, c = map(int, input().split())
    print(max(a, b) + max(min(a, b), c))


if __name__ == '__main__':
    main()