import sys

input = sys.stdin.readline 

def closestPick(n, k, p):
    p.sort()

    top = [max(p[0]-1, k-p[-1]), min(p[0]-1, k-p[-1])]

    for i in range(1, n):
        tmps = [(p[i] - p[i-1]) // 2]
        tmps.append((p[i] - p[i-1] - 1) - tmps[-1])
        for tmp in tmps:
            if tmp >= top[0]:
                top[0], top[1] = tmp, top[0]
            elif tmp > top[1]:
                top[1] = tmp

    return sum(top) / k


def main():
    for t in range(int(input())):
        n, k = map(int, input().split())
        p = [int(v) for v in input().split()]
        print(f'Case #{t+1}: {closestPick(n, k, p)}')


if __name__ == '__main__':
    main()