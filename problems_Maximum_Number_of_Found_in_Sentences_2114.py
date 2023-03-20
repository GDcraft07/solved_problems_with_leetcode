class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        s = []
        for i in sentences:
            s.append(len(i.split()))

        return max(s)
