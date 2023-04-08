class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            count = numBottles % numExchange
            ans += (numBottles - count) // numExchange
            numBottles = ((numBottles - count) // numExchange) + count

        return ans


print(Solution().numWaterBottles(15, 4))