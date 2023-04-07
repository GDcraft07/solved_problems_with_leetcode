from math import ceil

#Формулу вывел сам, однако не знал про math.ceil

class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        sum_list = sum(nums)
        return ceil(abs((sum_list - goal) / limit))