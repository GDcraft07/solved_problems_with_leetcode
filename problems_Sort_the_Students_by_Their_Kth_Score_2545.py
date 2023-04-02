class Solution:
    def sortTheStudents(self, score: list[list[int]], k: int) -> list[list[int]]:
        new_socre = [[] for _ in range(len(score))]
        for count, i in enumerate(score):
            new_socre[count].append(i[k])
            new_socre[count].append(i)

        new_socre.sort()

        return [i[1] for i in new_socre][::-1]


print(Solution().sortTheStudents([[3,4],[5,6]], 0))