import sys

input = sys.stdin.readline 

def alienGen(g):
    n = 1
    res = 0
    while (n * (n-1) // 2) <= g:
        tmp = g - (n * (n-1) // 2)
        if tmp and (tmp / n) % 1 == 0:
            res += 1
        n += 1

    return res


def main():
    for t in range(int(input())):
        g = int(input())

        print(f'Case #{t+1}: {alienGen(g)}')


if __name__ == '__main__':
    main()