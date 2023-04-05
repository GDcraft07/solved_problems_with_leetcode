class Solution:
    def modifyString(self, s: str) -> str:
        if '?' in s:
            index = s.index('?')
            try:
                left = ord(s[index - 1])
            except IndexError:
                left = ord(s[index])
            try:
                right = ord(s[index + 1])
            except:
                right = ord(s[index])
            if left != 97 and right != 97:
                s = s[:index] + 'a' + s[index + 1:]

            elif left != 98 and right != 98:
                s = s[:index] + 'b' + s[index + 1:]

            else:
                s = s[:index] + 'c' + s[index + 1:]

        if '?' in s:
            return self.modifyString(s)
        else:
            return s
