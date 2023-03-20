class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        s = []
        for count, i in enumerate(nums):
            s.append(i)
            nums[count] = sum(s)
        return nums
