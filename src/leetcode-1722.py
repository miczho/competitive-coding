'''
#union-find
'''

import sys
from typing import List
from collections import Counter

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n, ans = len(source), 0
        parent, grp1, grp2 = [i for i in range(n)], [[] for _ in range(n)], [[] for _ in range(n)]


        # know this
        def union(x, y):
        	parent[find(x)] = find(y)

        # know this
        def find(x):
        	if parent[x] != x: parent[x] = find(parent[x])
        	return parent[x]


        for i, j in allowedSwaps:
        	union(i, j)

        for i in range(n):
        	parent[i] = find(parent[i])
        	grp1[parent[i]].append(source[i])
        	grp2[parent[i]].append(target[i])
        
        for i in range(n):
        	diff = Counter(grp1[i]) - Counter(grp2[i])
        	ans += sum(diff.values())
            
        return ans

def main():
    s = Solution()
    print(s.minimumHammingDistance([1,2,3,4], [2,1,4,5], [[0,1],[2,3]]))

if __name__ == "__main__":
    main()