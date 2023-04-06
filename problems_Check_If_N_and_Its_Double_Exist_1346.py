class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                pivot = arr[i] // 2

                if pivot in arr[i + 1:] or pivot in arr[:i]:
                    return True

        return False


print(Solution().checkIfExist([-2, 0, 10, -19, 4, 6, -8]))