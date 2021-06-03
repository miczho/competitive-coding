class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)
        ans = 0

        psum = [0]
        for x in stones:
            psum.append(psum[-1] + x)

        dp = dict()
        def dfs(pos, turn):
            if pos >= n-1: return 0

            if (pos, turn) not in dp:
                if turn == 0:
                    res = float('-inf')
                    for i in range(pos+1, n):
                        res = max(res, psum[i+1] + dfs(i, turn^1))
                else:
                    res = float('inf')
                    for i in range(pos+1, n):
                        res = min(res, -psum[i+1] + dfs(i, turn^1))

                dp[(pos, turn)] = res

            return dp[(pos, turn)]

        return dfs(0, 0)