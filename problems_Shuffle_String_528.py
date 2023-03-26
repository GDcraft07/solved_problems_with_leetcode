class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        lib = {}

        for index, i in enumerate(s):
            running = True
            while running:
                if i in lib:
                    i += ' '
                else:
                    lib[i] = indices[index]
                    running = False

        lib = {k: v for k, v in sorted(lib.items(), key=lambda item: item[1])}
        new_word = ''
        for name, _ in lib.items():
            if len(name) > 1:
                new_word += name[0]
            else:
                new_word += name

        return new_word
