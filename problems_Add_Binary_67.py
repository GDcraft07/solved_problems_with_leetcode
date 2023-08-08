class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sums = str(bin(int(a, 2) + int(b, 2)))[2:]
        return sums
