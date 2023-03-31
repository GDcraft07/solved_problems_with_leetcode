class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        dot = int(len(nums) / 2)
        left_list = nums[:dot]
        result_num = []
        if len(nums) % 2 == 0:
            right_list = nums[dot:]
            for i in range(len(left_list)):
                result_num.append(str(left_list[i]) + str(right_list[-(i + 1)]))

            result_num = list(map(int, result_num))

            return sum(result_num)

        else:
            right_list = nums[dot + 1:]
            print(left_list, right_list)
            mid_number = nums[dot]
            for i in range(len(left_list)):
                result_num.append(str(left_list[i]) + str(right_list[-(i + 1)]))

            print(result_num)

            result_num = list(map(int, result_num))

            return sum(result_num) + mid_number
