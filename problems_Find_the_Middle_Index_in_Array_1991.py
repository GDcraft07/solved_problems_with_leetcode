class Solution:
    def findMiddleIndex(self, nums):
        for count, i in enumerate(nums):
            sums_1 = sum([nums[i] for i in range(count)])

            sums_2 = sum(nums) - sums_1 - i
            if sums_1 == sums_2:
                return count

        return -1
