class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing_numbers = [i for i in range(arr[-1]) if i not in arr]
        if len(missing_numbers) > k:
            return missing_numbers[k]
        return arr[-1] - len(missing_numbers) + k + 1


print(Solution().findKthPositive([2,3,4,7,11], 5))