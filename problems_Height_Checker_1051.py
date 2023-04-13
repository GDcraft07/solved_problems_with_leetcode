class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        count = 0
        normal = sorted(heights)
        for i in range(len(heights)):
            if normal[i] != heights[i]:
                count += 1

        return count