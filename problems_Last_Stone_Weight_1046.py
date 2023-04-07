class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] != stones[-2]:
                stones.append(abs(stones[-1] - stones[-2]))

                stones.pop(-2)
                stones.pop(-2)
            else:
                stones.pop(-1)
                stones.pop(-1)

        return stones[0] if len(stones) == 1 else 0


print(Solution().lastStoneWeight([2, 2]))