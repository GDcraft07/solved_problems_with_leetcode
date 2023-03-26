class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        new_arrays = [nums[2 * i + 1] for i in range(int(len(nums) / 2)) for _ in range(nums[2 * i])]
        return new_arrays


print(Solution().decompressRLElist([1, 1, 2, 3]))
