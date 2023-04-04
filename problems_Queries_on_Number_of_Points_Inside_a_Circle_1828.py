class Solution:
    def countPoints(self, points: list[list[int]], queries: list[list[int]]) -> list[int]:
        ans = []

        for i in queries:
            count = 0
            for j in points:
                if (j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2 <= i[2] ** 2:
                    count += 1
            ans.append(count)

        return ans
