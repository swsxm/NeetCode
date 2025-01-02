# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, left, right):
            if not root:
                return True
            if not (left < root.val < right):
                return False
            return helper(root.left, left, root.val) and helper(
                root.right, root.val, right
            )

        return helper(root, float("-inf"), float("inf"))

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)

    def isValid(self, node):
        if not node:
            return True
        if not self.isLeftValid(node.left, node.val):
            return False
        if not self.isRightValid(node.right, node.val):
            return False
        return self.isValid(node.left) and self.isValid(node.right)

    def isLeftValid(self, node, val):
        if not node:
            return True
        if node.val >= val:
            return False
        return self.isLeftValid(node.left, val) and self.isLeftValid(node.right, val)

    def isRightValid(self, node, val):
        if not node:
            return True
        if node.val <= val:
            return False
        return self.isRightValid(node.left, val) and self.isRightValid(node.right, val)
