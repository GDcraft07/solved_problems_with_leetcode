class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        count = 10000000000
        if 1 not in nums:
            if len(nums) >= k:
                return True
            return False
        for i in range(nums.index(1), len(nums)):
            if nums[i] == 1:
                if count < k:
                    return False
                count = 0

            else:
                count += 1

        return True