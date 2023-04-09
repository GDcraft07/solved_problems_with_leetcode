class Solution:
    def isPalindrome(self, s: str) -> bool:
        alf = 'abcdefghijklmnopqrstuvwxyz1234567890'
        new_s = ''
        for i in s:
            if i in alf:
                new_s += i

        if new_s[::-1] == new_s:
            return True
        return False