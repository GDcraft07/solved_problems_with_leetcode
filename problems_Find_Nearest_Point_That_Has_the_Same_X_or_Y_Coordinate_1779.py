class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        min_sum = 10000000
        ans = -1
        for count, i in enumerate(points):
            if (i[0] == x or i[1] == y) and abs(x - i[0]) + abs(y - i[1]) < min_sum:
                min_sum = abs(x - i[0]) + abs(y - i[1])
                ans = count

        return ans
