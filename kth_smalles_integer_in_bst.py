# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        val = root.val

        def dfs(root):
            if not root:
                return
            nonlocal k, val
            dfs(root.left)
            k -= 1
            if k == 0:
                val = root.val
            dfs(root.right)

        dfs(root)
        return val
