class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        nums_1 = [i for i in nums if i < pivot]
        nums_2 = [i for i in nums if i > pivot]
        count = sum([1 for i in nums if i == pivot])

        return nums_1 + [pivot] * count + nums_2
