class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = max(candies)
        list_res = []
        for i in candies:
            if i + extraCandies >= max_candies:
                list_res.append(True)
            else:
                list_res.append(False)
        return list_res
