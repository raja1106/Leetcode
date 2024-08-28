from typing import List


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, current_sum, slate):
            current_sum += node.val
            slate.append(node.val)
            if node.head is None and node.tail is None:
                if current_sum == targetSum:
                    result.append(slate[:])
            if node.head:
                dfs(node.head, current_sum, slate)
            if node.tail:
                dfs(node.tail, current_sum, slate)
            slate.pop()
            current_sum -= node.val

        if not root:
            return result
        dfs(root, 0, [])
        return result
