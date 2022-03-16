class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        splits = [0]
        d = {}
        
        
        def dfs(split=0, size=0):
            if split == len(splits)-1: return 0
            
            if (split, size) not in d:
                print(split, size)
                l, r = splits[split]-1, splits[split+1]
                d[(split, size)] = dfs(split+1, envelopes[r][1]-1)
                while l + 1 != r:
                    m = (l + r) // 2
                    if envelopes[m][1] > size:
                        r = m
                    else:
                        l = m
                print(envelopes[r][1])
                if r != splits[split+1]:
                    d[(split, size)] = max(d[(split, size)], 1 + dfs(split+1, envelopes[r][1]))
            
            return d[(split, size)]
        
        
        envelopes.sort()
        print(envelopes)

        for i in range(1, n):
            if envelopes[i-1][0] != envelopes[i][0]:
                splits.append(i)
        splits.append(n)
        
        return dfs()
        # return dfs(0, envelopes[0][1])
        