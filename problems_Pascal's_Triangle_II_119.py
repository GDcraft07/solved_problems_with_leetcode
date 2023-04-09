class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        ans = [[1]]
        for i in range(rowIndex):
            temp = [0] + ans[-1] + [0]
            row = []
            for j in range(len(temp) - 1):
                row.append(temp[j] + temp[j + 1])
            ans.append(row)
        return ans[-1]
