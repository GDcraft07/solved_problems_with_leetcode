class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while left <= right:
            mid = (right + left) // 2
            if mid ** 2 == x:
                return mid
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid + 1
        return right


print(Solution().mySqrt(8))