class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left, right + 1):
            str_num = list(map(int, list(str(i))))
            running = True
            for j in str_num:
                try:
                    if i % j != 0:
                        running = False
                except ZeroDivisionError:
                    running = False
            if running:
                ans.append(i)

        return ans