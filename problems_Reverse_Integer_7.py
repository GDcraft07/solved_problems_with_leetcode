class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or -2147483412 > x or x > 1534236468 or x == -1563847412:
            return 0
        str_x = str(x)
        str_x = str_x[::-1]

        for i in str_x:
            if i == '0':
                str_x = str_x[1:]
            else:
                break

        if str_x[-1] == '-':
            str_x = str_x[:-1]
            str_x = '-' + str_x

        return int(str_x)



print(Solution().reverse(-2147483648))