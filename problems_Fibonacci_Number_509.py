class Solution:
    def fib(self, n: int) -> int:
        if n in [1, 2]:
            return 1
        if n == 0:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]
