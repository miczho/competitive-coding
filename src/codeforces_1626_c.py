import sys

input = sys.stdin.readline 

def monstersAndSpells(n, k, h):
    ans = 0

    # time, health
    tmp = [k[-1], h[-1]]
    for i in range(n-2, -1, -1):
        if tmp[0] - k[i] >= tmp[1]:
            ans += tmp[1] * (tmp[1]+1) // 2
            tmp = [k[i], h[i]]
        else:
            tmp[1] += max(0, h[i] - tmp[1] + tmp[0] - k[i])
    ans += tmp[1] * (tmp[1]+1) // 2

    return ans


def main():
    for _ in range(int(input())):
        n = int(input())
        k = [int(v) for v in input().split()]
        h = [int(v) for v in input().split()]

        print(monstersAndSpells(n, k, h))


if __name__ == '__main__':
    main()