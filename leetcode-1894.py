class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        n = len(chalk)
        
        for i in range(1, n):
            chalk[i] += chalk[i-1]
            
        k %= chalk[-1]
        
        for i in range(n):
            if chalk[i] > k: return i