class Solution:
    def search(self, nums: list[int], target: int) -> int:
        high = len(nums) - 1
        low = 0

        while low <= high:
            mid = (low - high) / 2
            guess = nums[int(mid)]
            if guess == target:
                if mid < 0:
                    return len(nums) + int(mid) + 1
                return int(mid)
            if guess > target:
                high = int(mid) - 1
            else:
                low = int(mid) + 1
        return -1
