class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s

        s = list(s)
        left = -k
        right = 0
        new_s = []
        while right < len(s):
            left += k
            right += k
            new_s.append(s[left:right])

        s.clear()
        for i in new_s:
            s.append(sum(list(map(int, i))))

        s = ''.join(list(map(str, s)))

        if len(s) <= k:
            return s

        return self.digitSum(s, k)

print(Solution().digitSum("233", 3))