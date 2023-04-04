class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        ans = nums[0]

        for i in range(1, len(nums)):
            if (abs(ans) > abs(nums[i])) or (abs(ans) == abs(nums[i]) and nums[i] > ans):
                ans = nums[i]

        return ans
