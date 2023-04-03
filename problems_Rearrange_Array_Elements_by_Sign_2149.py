class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        nums_1, nums_2, ans = [], [], []

        for i in nums:
            if i > 0:
                nums_1.append(i)
            if i < 0:
                nums_2.append(i)

        for i in range(len(nums) // 2):
            ans.append(nums_1[i])
            ans.append(nums_2[i])

        return ans
