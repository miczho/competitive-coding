import sys

input = sys.stdin.readline 

def pow(a, b, c):
    if c % 2 == 0:
        a = abs(a)
        b = abs(b)

    if a == b:
        return '='
    elif a > b:
        return '>'
    else:
        return '<'


def main():
    a, b, c = map(int, input().split())

    print(pow(a, b, c))


if __name__ == '__main__':
    main()