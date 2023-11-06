from typing import Optional
from structures.TreeNode import TreeNode


class Solution:
    max_depth = 0

    def backtrack(self, node, current_depth):
        if node == None:
            return

        current_depth += 1

        self.max_depth = max(self.max_depth, current_depth)

        if node.left:
            self.backtrack(node.left, current_depth)

        if node.right:
            self.backtrack(node.right, current_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.backtrack(root, 0)
        return self.max_depth
