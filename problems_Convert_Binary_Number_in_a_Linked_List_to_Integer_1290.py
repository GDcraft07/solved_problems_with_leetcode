class Solution:
    def getDecimalValue(self, head) -> int:
        if head is None:
            return 0

        ans = ''
        while head:
            ans += str(head.val)
            head = head.next

        ans = int(ans, 2)

        return ans
