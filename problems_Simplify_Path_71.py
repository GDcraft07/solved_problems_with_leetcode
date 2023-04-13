class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = []
        split_path = path.split('/')
        for i in range(len(split_path)):
            if split_path[i] != '' and split_path[i] != '.':
                if split_path[i] != '..':
                    ans.append(split_path[i])
                else:
                    if ans:
                        ans.pop()

        return '/' + '/'.join(ans)


print(Solution().simplifyPath("/home/"))