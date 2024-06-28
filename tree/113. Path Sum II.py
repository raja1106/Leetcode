from typing import List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, current_sum, slate):
            current_sum += node.val
            slate.append(node.val)
            if node.left is None and node.right is None:
                if current_sum == targetSum:
                    result.append(slate[:])
            if node.left:
                dfs(node.left, current_sum, slate)
            if node.right:
                dfs(node.right, current_sum, slate)
            slate.pop()
            current_sum -= node.val

        if not root:
            return result
        dfs(root, 0, [])
        return result
