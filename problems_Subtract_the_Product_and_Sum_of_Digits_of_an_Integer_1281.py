class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lists = list(str(n))
        lists = list(map(int, lists))
        sums = sum(lists)
        mult = 1
        for i in lists:
            mult *= i

        return mult - sums
