class Solution:
    def partitionString(self, s: str) -> int:
        ans = ['']

        left = 0

        while left <= len(s) - 1:
            if s[left] not in ans[-1]:
                ans[-1] += s[left]

            else:
                ans.append('')
                ans[-1] += s[left]

            left += 1

        return len(ans)
