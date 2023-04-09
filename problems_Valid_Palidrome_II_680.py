class Solution:
    def check_palidrome(self, s):
        if s[::-1] == s:
            print(s)
            return True
        return False

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                ans_1 = self.check_palidrome(s[:left] + s[left + 1:])
                ans_2 = self.check_palidrome(s[:right] + s[right + 1:])
                return ans_1 or ans_2
            left += 1
            right -= 1

        return True


print(Solution().validPalindrome("abc"))