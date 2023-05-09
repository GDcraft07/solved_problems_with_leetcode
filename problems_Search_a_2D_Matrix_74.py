class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix[0]) - 1
        n = 0
        while m >= 0 and n < len(matrix):
            if matrix[n][m] > target:
                m -= 1
            elif matrix[n][m] < target:
                n += 1
            else:
                return True
        return False
