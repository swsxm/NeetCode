# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        stack = deque([root])
        ret = []
        while stack:
            sub_list = []
            for _ in stack:
                element = stack.popleft()
                if element.left is not None:
                    stack.append(element.left)
                if element.right is not None:
                    stack.append(element.right)
                sub_list.append(element.val)
            ret.append(sub_list)
        return ret
