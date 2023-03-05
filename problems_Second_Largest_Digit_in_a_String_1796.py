class Solution:
    def secondHighest(self, s: str) -> int:
        arr = []
        for i in s:
            try:
                if int(i) not in arr:
                    arr.append(int(i))

            except ValueError:
                pass

        arr.sort()
        return arr[-2] if len(arr) > 1 else -1