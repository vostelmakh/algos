from typing import Optional
from structures.TreeNode import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = list()
        prev_value = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if prev_value is not None and root.val <= prev_value:
                return False

            prev_value = root.val
            root = root.right

        return True


class RecursionSolution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def solve(root, min_val, max_val):
            if root is None:
                return True

            if root.val <= min_val or root.val >= max_val:
                return False

            left = solve(root.left, min_val, root.val)
            right = solve(root.right, root.val, max_val)
            return left and right

        return solve(root, float('-inf'), float('inf'))


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(6)
root.left.left = None
root.left.right = None
root.right.left = TreeNode(3)
root.right.right = TreeNode(7)

solution = Solution()

is_valid_bst = solution.isValidBST(root)
print(is_valid_bst)
