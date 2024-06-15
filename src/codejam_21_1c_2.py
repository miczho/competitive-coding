'''
https://codingcompetitions.withgoogle.com/codejam/round/00000000004362d7/00000000007c0f01

#favorite
'''

import sys

input = sys.stdin.readline 

def roaringYears(y):
    n = len(str(y))
    ans = float('inf')

    def findNum(val, sections):
        res = []
        for _ in range(sections):
            res.append(str(val))
            val += 1
        return int(''.join(res))

    # why n+2?
    for i in range(2, n+2):
        l = 0
        r = 10 ** (n // i)
        while l + 1 < r:
            m = l + (r - l) // 2
            if findNum(m, i) > y:
                r = m
            else:
                l = m

        ans = min(ans, findNum(r, i))

    return ans


def main():
    for t in range(int(input())):
        y = int(input())
        print(f'Case #{t+1}: {roaringYears(y)}')


if __name__ == '__main__':
    main()