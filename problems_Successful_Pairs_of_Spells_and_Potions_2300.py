# Моё решение:
class Solution:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        ans = [0 for _ in range(len(spells))]
        potions = sorted(potions)
        for count, j in enumerate(spells):
            ans[count] = sum(1 for i in potions if j * i >= success)

        return ans

# Не мое решение:
class SolutiOn:
    def successfulPairs(self, spells: list[int], potions: list[int], success: int) -> list[int]:
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()
        for i in range(n):
            spell = spells[i]
            left = 0
            right = m - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs[i] = m - left
        return pairs