class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""

        for i in range(0, len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if ans == "":
                    ans = num[i] * 3

                else:
                    if int(ans[0]) < int(num[i]):
                        ans = num[i] * 3

        return ans


print(Solution().largestGoodInteger("23001119"))