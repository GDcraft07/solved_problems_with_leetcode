class Solution:
    def pivotInteger(self, n: int) -> int:
        list_of_n = [i for i in range(1, n + 1)]
        for i in list_of_n:
            if sum(list_of_n[:i]) == sum(list_of_n[i - 1:]):
                return i
        return -1
