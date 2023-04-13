class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = []
        not_ans = []
        for i in nums:
            if i not in not_ans:
                if i not in ans:
                    ans.append(i)
                else:
                    ans.remove(i)
                    not_ans.append(i)
        return ans[0]
