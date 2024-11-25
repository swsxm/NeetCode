# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if root.val == subRoot.val and self.check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def check(self, root, subRoot):
        if root is None or subRoot is None:
            return root == subRoot
        if root.val != subRoot.val:
            return False
        return self.check(root.left, subRoot.left) and self.check(
            root.right, subRoot.right
        )
