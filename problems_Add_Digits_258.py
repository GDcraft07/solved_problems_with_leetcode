class Solution:
    def addDigits(self, num: int) -> int:
        sums = sum(list(map(int, list(str(num)))))

        if sums < 10:
            return sums

        return self.addDigits(sums)
