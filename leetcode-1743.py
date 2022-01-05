from collections import defaultdict

class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        def dfs(parent, curr):
            ans.append(curr)
            for child in d[curr]:
                if child != parent:
                    dfs(curr, child)

        d = defaultdict(list)
        ans = []
        
        for a in adjacentPairs:
            d[a[0]].append(a[1])
            d[a[1]].append(a[0])

        for key, val in d.items():
            if len(val) == 1:
                dfs(float("inf"), key)
                break

        return ans