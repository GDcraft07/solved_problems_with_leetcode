class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = len(range(0, abs(dividend) - abs(divisor) + 1, abs(divisor)))
        if divisor < 0:
            count = -count

        if dividend < 0:
            count = -count

        result = min(count, 2 ** 31 - 1)
        result = max(result, -2 ** 31)

        return result


print(Solution().divide(-6, 3))