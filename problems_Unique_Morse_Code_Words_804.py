class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morze = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        morze_words = []

        for i in words:
            word = ''
            for j in i:
                word += morze[ord(j) - 97]

            morze_words.append(word)

        sets = set(morze_words)

        return len(sets)
