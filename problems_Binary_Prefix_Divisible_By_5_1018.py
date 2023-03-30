class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        str_nums = list(map(str, nums))
        str_num = []
        bool_nums = []
        for i in range(len(str_nums)):
            new_number = ''.join(str_nums[:i + 1])
            str_num.append(new_number)

        for i in str_num:
            if int(i, 2) % 5 == 0:
                bool_nums.append(True)
            else:
                bool_nums.append(False)

        return bool_nums
