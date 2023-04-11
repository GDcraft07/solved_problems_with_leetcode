class Solution:
    def removeStars(self, s: str) -> str:
        list_s = list(s)
        ans = []
        for i in list_s:
            if i != '*':
               ans.append(i)
            else:
                ans.pop(-1)

        ans = ''.join(ans)
        return ans

print(Solution().removeStars("leet**cod*e"))