import sys

input = sys.stdin.readline 

def main():
    a, b, c, d = map(int, input().split())

    for i in range(1, 200001):
        if ((a + (i * b)) / (i * c)) <= d:
            print(i)
            break
        elif i == 200000:
            print(-1)


if __name__ == '__main__':
    main()