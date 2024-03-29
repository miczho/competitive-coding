class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        n = len(envelopes)
        tails = []
        
        for e in envelopes:
            l, r = -1, len(tails)
            
            while l + 1 < r:
                m = l + (r - l) // 2
                if tails[m] >= e[1]:
                    r = m
                else:
                    l = m
            
            if r == len(tails):
                tails.append(e[1])
            else:
                tails[r] = e[1]
        
        return len(tails)
