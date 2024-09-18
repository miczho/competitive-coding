"""
#interview
"""

import sys, random, time

def meanderingArray(unsorted):
    unsorted.sort()
    n, ans = len(unsorted), []
    for i in range(n//2):
        ans.append(unsorted[-i-1]), ans.append(unsorted[i])
    if n & 1: ans.append(unsorted[n//2])
    return ans

def main():
    print(meanderingArray([1,-2,3]))

if __name__ == "__main__":
    main()
