class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        dicts = {i: 0 for i in list(map(str, arr))}
        for i in arr:
            dicts[str(i)] += 1

        sorted_dict = {k: v for k, v in sorted(dicts.items(), key=lambda item: item[1])}
        for key in list(sorted_dict):
            if sorted_dict[key] <= k:
                k -= sorted_dict[key]
                del sorted_dict[key]

            else:
                break

        return len(sorted_dict)


print(Solution().findLeastNumOfUniqueInts(arr=[5, 5, 4], k=1))