class Solution:
    def maxDepth(self, root) -> int:
        def count(roots, counts):
            if not roots:
                return counts
            return max(count(roots.left, counts + 1), count(roots.right, counts + 1))

        return count(root, 0)
