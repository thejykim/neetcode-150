class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = list(range(len(cost) + 1))

        dp[0] = 0
        dp[1] = 0

        for n in range(2, len(cost) + 1):
            dp[n] = min(dp[n - 2] + cost[n - 2], dp[n - 1] + cost[n - 1])
        
        return dp[len(cost)]