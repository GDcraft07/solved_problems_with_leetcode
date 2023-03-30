class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even_list = []
        odd_list = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even_list.append(nums[i])
            else:
                odd_list.append(nums[i])

        ans = []

        for i in range(len(even_list)):
            ans.append(even_list[i])
            ans.append(odd_list[i])

        return ans
