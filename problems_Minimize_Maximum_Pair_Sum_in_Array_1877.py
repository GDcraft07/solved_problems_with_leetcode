class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        sums = []

        while left <= right:
            sums.append(nums[left] + nums[right])
            left += 1
            right -= 1

        return max(sums)
