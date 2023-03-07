class Solution:
    def shuffle(self, nums: list[int], n: int):
        new_arr = [(nums[i], nums[n+i]) for i in range(n)]
        new_arr = [j for i in new_arr for j in i]
        return new_arr
