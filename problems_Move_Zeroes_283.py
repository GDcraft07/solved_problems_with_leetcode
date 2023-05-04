class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count_zero = nums.count(0)
        for i in range(count_zero):
            nums.remove(0)
            nums.append(0)