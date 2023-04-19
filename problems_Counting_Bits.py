class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = []
        for i in range(0, n + 1):
            ans.append(sum(list(map(int, list(bin(i))[2:]))))

        return ans