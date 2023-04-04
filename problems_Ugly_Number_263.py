class Solution:
    def isUgly(self, n: int) -> bool:
        while True:
            if n % 2 == 0:
                n /= 2
            if n % 3 == 0:
                n /= 3
            if n % 5 == 0:
                n /= 5

            if n == 1:
                return True

            if (n % 2 != 0 and n % 3 != 0 and n % 5 != 0) or n == 0:
                return False


print(Solution().isUgly(0))