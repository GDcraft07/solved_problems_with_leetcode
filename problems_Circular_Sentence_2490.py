class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()

        if sentence[0][0] != sentence[-1][-1]:
            return False

        for i in range(0, len(sentence) - 1):
            if sentence[i][-1] != sentence[i + 1][0]:
                return False

        return True


print(Solution().isCircularSentence('Leetcode is cool'))