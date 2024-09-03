# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = 1
        stack = [(root, level)]
        hash_map = {}
        while stack:
            node, level = stack.pop()
            if level not in hash_map:
                hash_map[level] = node.val
            level += 1
            if node.left:
                stack.append((node.left, level))
            if node.right:
                stack.append((node.right, level))

        return list(hash_map.values())

s = Solution()
b = TreeNode(4)
c = TreeNode(2, left=b)
d = TreeNode(3)
a = TreeNode(1, left=c, right=d)
print(s.rightSideView(a))
