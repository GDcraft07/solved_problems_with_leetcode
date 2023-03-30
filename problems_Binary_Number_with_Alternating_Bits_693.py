class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_number_list = list(str(bin(n)))
        for i in range(len(bin_number_list)):
            if i != 0 and i != len(bin_number_list):
                try:
                    if bin_number_list[i - 1] == bin_number_list[i] or bin_number_list[i + 1] == bin_number_list[i]:
                        return False
                except IndexError:
                    pass
        if len(bin_number_list) == 2:
            if set(bin_number_list) != 2:
                return False

        return True


print(Solution().hasAlternatingBits(5))