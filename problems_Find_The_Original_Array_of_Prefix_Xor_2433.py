class Solution:
    def xor(self, num_1, xors):
        num_1 = list(str(bin(num_1)))[2:]
        xors = list(str(bin(xors)))[2:]
        if len(xors) > len(num_1):
            num_1 = ['0'] * (len(xors) - len(num_1)) + num_1
        if len(xors) < len(num_1):
            xors = ['0'] * (len(num_1) - len(xors)) + xors
        num_2 = ''
        for i in range(len(num_1)):
            num_2 += str(int(xors[i]) ^ int(num_1[i]))

        return int(num_2, 2)

    def findArray(self, pref: list[int]) -> list[int]:
        ans = [pref[0]]
        for i in range(1, len(pref)):
            ans.append(self.xor(pref[i - 1], pref[i]))

        return ans


print(Solution().findArray([413935,351122]))