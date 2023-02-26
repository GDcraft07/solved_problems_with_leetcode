class Solution:
    def numIdenticalPairs(self, nums):
        return sum([i == j and count_1 < count_2 for count_1, i in enumerate(nums) for count_2, j in enumerate(nums)])
