class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        min_of_matrix = [min(i) for i in matrix]
        ans = []
        for count, i in enumerate(matrix):
            countes = i.index(min_of_matrix[count])
            alls = []
            for j in matrix:
                if j[countes] <= min_of_matrix[count]:
                    alls.append(True)
                else:
                    alls.append(False)
            if all(alls):
               ans.append(min_of_matrix[count])

        return ans


print(Solution().luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))