class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sums = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sums += nums[i]

        return sums


print(Solution().arrayPairSum([6,2,6,5,1,2]))