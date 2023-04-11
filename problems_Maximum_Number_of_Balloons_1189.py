class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_letters = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        balloon_letters_in_text = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for i in text:
            if i in 'balon':
                balloon_letters_in_text[i] += 1

        ans = []
        for name, key in balloon_letters_in_text.items():
            ans.append(key // balloon_letters[name])

        return min(ans)