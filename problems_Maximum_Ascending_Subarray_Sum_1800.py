class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        ascending = [[nums[0]]]

        for i in range(1, len(nums)):
            if nums[i] > ascending[-1][-1]:
                ascending[-1].append(nums[i])
            else:
                ascending.append([nums[i]])
        print(ascending)
        ans = max(list(map(sum, ascending)))

        return ans


print(Solution().maxAscendingSum([3, 6, 10, 1, 8, 9, 9, 8, 9]))