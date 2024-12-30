# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        output = []
        while stack:
            output.append(stack[-1].val)
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
        return output

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level_check = set()
        output = []

        def dfs(node, level):
            if not node:
                return
            if level not in level_check:
                level_check.add(level)
                output.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

        dfs(root, 1)
        return output
