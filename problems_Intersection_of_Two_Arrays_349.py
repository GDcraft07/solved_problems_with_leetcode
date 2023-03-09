class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums3 = []

        for i in nums2:
            if (i in nums1) and (i not in nums3):
                nums3.append(i)

        return nums3
