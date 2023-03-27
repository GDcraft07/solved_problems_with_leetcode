class Solution:
    def sortSentence(self, s: str) -> str:
        ans = ''
        new_arr = [[i[:-1], int(i[-1])] for i in s.split()]
        new_arr.sort(key=lambda x: x[-1])
        for count, i in enumerate(new_arr):
            if count == len(new_arr) - 1:
                ans += i[0]
            else:
                ans += f'{i[0]} '

        return ans


print(Solution().sortSentence("is2 sentence4 This1 a3"))
