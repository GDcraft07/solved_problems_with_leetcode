class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        dp = [0] * (len(cost) + 1)
        dp[1] = cost[0]
        for i in range(2, len(cost) + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])

        return min(dp[-1], dp[-2])
