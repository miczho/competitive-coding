'''
#dp #knapsack
'''

import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n, INF = len(coins), float('inf')
        dp = [INF] * (amount+1)
        dp[0] = 0
        
        for i in coins:
            try: dp[i] = 1
            except: continue
        
        for i in range(1, amount+1):
            for j in range(n):
                if i + coins[j] <= amount:
                    dp[i + coins[j]] = min(dp[i + coins[j]], dp[i] + 1)
        
        if dp[amount] == INF:
            return -1
        return dp[amount]

def main():
    pass

if __name__ == "__main__":
    main()