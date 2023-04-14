class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        frequency = {i: nums.count(i) for i in set(nums)}
        frequency = dict(sorted(frequency.items(), key=lambda x: x[0], reverse=True))
        print(frequency)
        ans = []
        while frequency:
            name = min(frequency, key=frequency.get)
            for i in range(frequency[name]):
                ans.append(name)
            del frequency[name]
        return ans


print(Solution().frequencySort([1, 3, 3, 2, 2]))