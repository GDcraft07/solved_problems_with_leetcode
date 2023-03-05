class Solution:
    def canBeEqual(self, target: list[int], arr: list[int]) -> bool:
        target.sort()
        arr.sort()
        count = len(target)

        for i in range(count):
            if target[i] != arr[i]:
                return False
        return True
