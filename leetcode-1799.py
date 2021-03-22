import sys

class Solution(object):
    @lru_cache(None)
    def gcd(self, a, b):
        while b != 0: a, b = b, a%b
        return a

    def maxScore(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n, dp = len(nums) // 2, {}

        def dfs(x, mask):
            if x == n+1: return 0

            if (x, mask) not in dp:
                for i in range(2*n):
                    if (1 << i) & mask: continue
                    for j in range(i+1, 2*n):
                        if (1 << j) & mask: continue
                        tmp = (x * self.gcd(nums[i], nums[j])) + dfs(x+1, (mask | (1 << i)) | (1 << j))
                        dp[(x, mask)] = max(dp.get((x, mask), 0), tmp)
            return dp[(x, mask)]

        return dfs(1, 0)


def main():
    s = Solution()
    print(s.maxScore([1, 2]))


if __name__ == "__main__":
    main()