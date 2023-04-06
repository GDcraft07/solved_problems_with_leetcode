class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        ans = sorted(nums)
        re_ans = reversed(ans)
        return ans == nums or list(re_ans) == nums
