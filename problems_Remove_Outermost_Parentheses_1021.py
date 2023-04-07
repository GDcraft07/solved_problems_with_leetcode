class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        front = 0
        back = 0
        index = 0
        ans = ''
        for i in s:
            if i == '(':
                front += 1

            else:
                back += 1

            if front == back:
                ans += s[index + 1: front + back - 1]
                index = front + back

        return ans


print(Solution().removeOuterParentheses("(()())(())"))