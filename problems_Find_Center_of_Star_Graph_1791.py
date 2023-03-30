class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        lists = []

        for i in edges:
            if edges[0][0] in i:
                lists.append(True)
            else:
                lists.append(False)
                break

        if all(lists):
            return edges[0][0]

        lists.clear()

        for i in edges:
            if edges[0][1] in i:
                lists.append(True)
            else:
                lists.append(False)
                break

        if all(lists):
            return edges[0][1]
