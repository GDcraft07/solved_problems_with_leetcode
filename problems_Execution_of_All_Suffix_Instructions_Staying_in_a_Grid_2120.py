class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 1
        count = 4
        for i in range(n - 1):
            ans = ans + count * (i + 1)

        return ans


print(Solution().coloredCells(6))