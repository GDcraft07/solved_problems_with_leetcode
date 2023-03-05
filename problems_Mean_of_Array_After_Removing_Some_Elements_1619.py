class Solution:
    def trimMean(self, arr):
        run = True
        time = int(len(arr) * 0.05)
        count = 0
        arr.sort()

        while run:

            arr.pop(0)
            arr.pop(-1)

            count += 1
            if count == time:
                run = False

        return round(sum(arr) / len(arr), 5)
