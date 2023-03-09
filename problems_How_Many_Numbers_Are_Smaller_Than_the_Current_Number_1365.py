class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        new_array = []

        count = 0
        for i in nums:
            for j in nums:
                if i > j:
                    count += 1

            new_array.append(count)
            count = 0

        return new_array
