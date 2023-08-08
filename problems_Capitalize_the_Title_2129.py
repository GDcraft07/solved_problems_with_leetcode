class Solution:
    def capitalizeTitle(self, title: str) -> str:
        new_word = []
        for i in title.split():
            if len(i) > 2:
                i = i.capitalize()
            else:
                i = i.lower()
            new_word.append(i)

        new_word = ' '.join(new_word)
        return new_word
