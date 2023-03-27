class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        count_1 = 0
        if ruleKey == "color":
            count_1 = 1
        if ruleKey == "name":
            count_1 = 2

        for i in items:
            if i[count_1] == ruleValue:
                count += 1

        return count
