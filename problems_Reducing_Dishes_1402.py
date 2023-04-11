class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        satisfaction.sort()
        satisfaction.reverse()

        count, ans = [0] * 2

        for i in satisfaction:
            count += i
            if count < 0:
                break
            ans += count

        return ans


print(Solution().maxSatisfaction([4, 3, 2]))