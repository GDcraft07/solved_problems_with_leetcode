class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        if num == 0:
            return 0

        while num != 0:
            if num % 2 == 0:
                step += 1
                num /= 2
            else:
                step += 2
                num -= 1
                num /= 2

        return step - 1