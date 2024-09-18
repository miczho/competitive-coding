"""
#interview
"""

import sys, random, time

def mergeArrays(a, b):
    m, n, p1, p2, ans = len(a), len(b), 0, 0, []
    while p1 != m or p2 != n:
        if p2 == n or a[p1] <= b[p2]:
            ans.append(a[p1])
            p1 += 1
        elif p1 == m or a[p1] > b[p2]:
            ans.append(b[p2])
            p2 += 1
    return ans

def main():
    print(mergeArrays([1,2,3], [2,5,5]))

if __name__ == "__main__":
    main()
