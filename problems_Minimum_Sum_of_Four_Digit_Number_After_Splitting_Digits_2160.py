class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = list(map(int, list(str(num))))
        num_list.sort()
        return int(str(num_list[0]) + str(num_list[2])) + int(str(num_list[1]) + str(num_list[3]))
