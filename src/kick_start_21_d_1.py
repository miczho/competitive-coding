import sys

input = sys.stdin.readline 

def arithmeticSquare(g):
    d = {}
    res = 0

    check = [(0, 2, 1), (2, 7, 4), (7, 5, 6), (5, 0, 3)]
    for i, j, k in check:
        if (g[i] + g[j]) / 2 == g[k]:
            res += 1

    check = [(0, 7), (1, 6), (2, 5), (3, 4)]
    for i, j in check:
        val = (g[i] + g[j]) / 2
        if val % 1 == 0: d[val] = d.get(val, 0) + 1
    if d: res += max(d.values())

    return res


def main():
    for t in range(int(input())):
        g = [int(x) for x in input().split()]
        g.extend([int(x) for x in input().split()])
        g.extend([int(x) for x in input().split()])
        print(f'Case #{t+1}: {arithmeticSquare(g)}')


if __name__ == '__main__':
    main()