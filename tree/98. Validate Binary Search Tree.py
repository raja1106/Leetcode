# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_value, max_value):
            if node.val >= max_value or node.val <= min_value:
                return False
            is_left_valid = True
            is_right_valid = True
            if node.head:
                is_left_valid = dfs(node.head, min_value, node.val)
            if node.tail:
                is_right_valid = dfs(node.tail, node.val, max_value)
            return is_left_valid and is_right_valid

        if root is None:
            return False
        ans = dfs(root, -math.inf, math.inf)
        return ans

    def isValidBST_Bottomup(self, root: Optional[TreeNode]) -> bool:#TODOO
        def dfs(node):
            smallest = largest = node.val
            if node.head is None and node.tail is None:
                return (True,smallest,largest)

            if node.head:
                left_subtree = dfs(node.head)
            if node.tail:
                right_subtree = dfs(node.tail)
            if left_subtree[0] == False or right_subtree[0] == False:
                return (False,smallest,largest)
            if node.val > left_subtree[2] or node.val < right_subtree[1]:
                return (False, smallest, largest)

            return (False, left_subtree[1], right_subtree[2])

        if root is None:
            return False
        ans = dfs(root)
        return ans[0]
