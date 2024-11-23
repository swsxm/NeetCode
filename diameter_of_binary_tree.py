# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        level = 0

        def get_depth(root):
            nonlocal level
            if not root:
                return 0
            left = get_depth(root.left)
            right = get_depth(root.right)
            level = max(level, left + right)
            return 1 + max(left, right)

        get_depth(root)
        return level
