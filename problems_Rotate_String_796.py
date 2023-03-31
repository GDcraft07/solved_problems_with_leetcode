class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s_list = list(s)
        goal_list = list(goal)
        for i in range(len(s_list)):
            if s_list == goal_list:
                return True
            pop_element = s_list.pop(0)
            s_list.append(pop_element)
        return False


print(Solution().rotateString("abcde", "cdeab"))
