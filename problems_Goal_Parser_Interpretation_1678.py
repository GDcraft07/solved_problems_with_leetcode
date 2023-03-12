class Solution:
    def interpret(self, command: str) -> str:
        new_word = ''
        list_command = list(command)
        for count, i in enumerate(list_command):
            if i == 'G':
                new_word += i

            if i == '(':
                if i + list_command[count + 1] == '()':
                    new_word += '\\u043e'

                else:
                    new_word += 'al'

        return new_word


print(Solution().interpret("G()(al)"))