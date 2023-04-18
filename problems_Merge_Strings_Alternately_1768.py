class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len_word = min(len(word1), len(word2))
        ans = ''
        for i in range(min_len_word):
            ans += word1[i]
            ans += word2[i]

        ans += word1[min_len_word:]
        ans += word2[min_len_word:]

        return ans