# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        has_path_sum = False
        def dfs(node, current_sum):
            nonlocal has_path_sum
            current_sum += node.val
            if not node.left and not node.right:
                if current_sum == targetSum:
                    has_path_sum = True
            if node.left and not has_path_sum:
                dfs(node.left, current_sum)
            if node.right and not has_path_sum:
                dfs(node.right, current_sum)
            current_sum -= node.val
        if not root:
            return False
        dfs(root,0)
        return has_path_sum
