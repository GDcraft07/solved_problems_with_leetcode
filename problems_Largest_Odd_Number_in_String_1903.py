class Solution:
    def largestOddNumber(self, num: str) -> str:
        list_of_num = list(map(int, list(num)))

        running = True

        while running:
            if list_of_num[-1] % 2 != 0:
                running = False
            else:
                list_of_num.pop(-1)
                if len(list_of_num) == 0:
                    running = False

        new_word = ''.join(list(map(str, list_of_num)))
        return new_word




print(Solution().largestOddNumber("26"))