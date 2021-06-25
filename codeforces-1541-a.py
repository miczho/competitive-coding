import sys

input = sys.stdin.readline 

def main():
    for t in range(int(input())):
        n = int(input())

        res = [i for i in range(1, n+1)]
        for i in range(n//2):
            res[2*i], res[2*i+1] = res[2*i+1], res[2*i]
        if n % 2:
            res[-1], res[-2] = res[-2], res[-1]
        print(*res)


if __name__ == '__main__':
    main()