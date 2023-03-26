class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        new_nums = [list(str(i)) for i in nums]
        new_new_nums = [sum(list(map(int, i))) for i in new_nums]

        return abs(sum(nums) - sum(new_new_nums))
