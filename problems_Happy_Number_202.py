class Solution:
    def isHappy(self, n: int, k=0) -> bool:
        if k == 7:
            return False

        res = sum(int(i) ** 2 for i in str(n))
        print(res)
        if res == 1:
            return True

        k += 1
        return self.isHappy(res, k)


print(Solution().isHappy(5783988))
