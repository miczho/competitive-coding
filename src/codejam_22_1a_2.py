"""
#incomplete
"""

import sys
from collections import defaultdict

input = sys.stdin.readline 

def equalSum(arr, size):
    n = len(arr)
    dp = defaultdict(lambda: (0, 0))
    res = []
    
    dp[0] = (1, -1)
    for i in range(n):
        for j in range(size, arr[i]-1, -1):
            dp[j] = (dp[j][0] | dp[j - arr[i]][0], j - arr[i])

    i = dp[size][1]
    while i != -1:
        res.append(size - i)
        size = i
        i = dp[size][1]

    return res


def main():
    for t in range(int(input())):
        n = int(input())
        arr = [i for i in range(1, n+1)]
        print(*arr, flush=True)
        arr.extend([int(x) for x in input().split()])
        print(*equalSum(arr, sum(arr)//2), flush=True)


if __name__ == '__main__':
    main()