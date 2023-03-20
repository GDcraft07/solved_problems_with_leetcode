class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for count, i in enumerate(nums):
                spis = []
                numbers = target - i
                if numbers in nums:
                    if count != nums.index(numbers):
                        spis.append(count)
                        spis.append(nums.index(numbers))
                        return spis
