from collections import defaultdict

def gcd(a, b):
    while b != 0:
        a, b = b, a
        b %= a
    return a
    
    
class Solution(object):
    def getCoprimes(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        coprimes = [set()]
        for i in range(1, 51):
            tmp = set()
            for j in range(1, 51):
                if gcd(i, j) == 1: tmp.add(j)
            coprimes.append(tmp)
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res, path = [float('-inf')]*len(nums), defaultdict(list)
        
        def dfs(parent, node, depth):
            res[node] = -1
            closest = -1
            for key, val in path.items():
                if val and (key in coprimes[nums[node]]):
                    if val[-1][1] > closest:
                        res[node] = val[-1][0]
                        closest = val[-1][1]
                        
            path[nums[node]].append((node, depth))
            for child in graph[node]:
                if parent != child:
                    dfs(node, child, depth+1)
            path[nums[node]].pop()
        
        
        dfs(-1, 0, 0)
        return res


s = Solution()
print(s.getCoprimes([2,3,3,2], [[0,1],[1,2],[1,3]]))