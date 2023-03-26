class Solution:
    def leftRigthDifference(self, nums: list[int]) -> list[int]:
        num = nums
        left_sum = [sum(num[:count]) for count in range(len(nums))]
        re_num = num[::-1]
        right_sum = [sum(re_num[:count]) for count in range(len(nums))][::-1]
        ans = [abs(left_sum[i] - right_sum[i]) for i in range(len(right_sum))]
        return ans
