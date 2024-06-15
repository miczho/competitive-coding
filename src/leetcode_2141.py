class Solution(object):
    def maxRunTime(self, n, batteries):
        """
        :type n: int
        :type batteries: List[int]
        :rtype: int
        """
        
        def isValid(avg):
            res = 0
            for b in batteries:
                res += min(avg, b)
            return res >= avg * n
        
        l, r = 1, sum(batteries) // n + 1
        while l + 1 != r:
            m = l + (r - l) // 2
            if isValid(m):
                l = m
            else:
                r = m
        
        return l
