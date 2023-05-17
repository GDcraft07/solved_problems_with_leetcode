class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]

        if n < 3:
            return dp[n]
        else:
            dp += [0] * (n - 2)

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


print(Solution().climbStairs(6))
