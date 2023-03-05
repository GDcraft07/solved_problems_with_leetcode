# Первый вариант
class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n % 2 == 0:
            return int(n / 2)
        return n


# Второй вариант
class Solutions:
    def numberOfCuts(self, n: int) -> int:
        res = int(n / 2) if n % 2 == 0 or n == 1 else n
        return res
