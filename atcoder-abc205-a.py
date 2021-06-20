import sys

input = sys.stdin.readline 

def main():
    a, b = map(float, input().split())

    print(a * b / 100)


if __name__ == '__main__':
    main()