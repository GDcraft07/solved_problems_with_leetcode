class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        litters = {i: 0 for i in set(list(map(str, nums)))}
        for i in nums:
            litters[str(i)] += 1
            if litters[str(i)] == 2:
                return i
