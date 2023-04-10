class Solution:
    def isValid(self, s: str) -> bool:
        list_of_valid = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                list_of_valid.append(i)
            else:
                if not list_of_valid:
                    return False
                if i == ')' and list_of_valid[-1] == '(':
                    list_of_valid.pop()
                elif i == ']' and list_of_valid[-1] == '[':
                    list_of_valid.pop()
                elif i == '}' and list_of_valid[-1] == '{':
                    list_of_valid.pop()
                else:
                    return False
        return not list_of_valid
