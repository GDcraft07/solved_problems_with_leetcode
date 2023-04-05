class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        new_num = str(num)
        left = 0
        right = k
        count = 0
        while right <= len(new_num):
            nums = int(new_num[left:right])
            if nums != 0:
                if num % nums == 0:
                    count += 1

            left += 1
            right += 1

        return count


print(Solution().divisorSubstrings(430043, 2))