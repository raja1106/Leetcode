# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Best_Readable:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            min_val = max_val = node.val
            if node.left is None and node.right is None:
                return min_val, max_val, True
            is_left_bst = is_right_bst = True
            if node.left:
                left_min_val, left_max_val, is_left_bst = dfs(node.left)
                min_val = left_min_val
                if left_max_val > node.val:
                    is_left_bst = False
            if node.right:
                right_min_val, right_max_val, is_right_bst = dfs(node.right)
                max_val = right_max_val
                if right_min_val < node.val:
                    is_right_bst = False
            if is_left_bst and is_right_bst and (min_val <= node.val <= max_val):
                return min_val, max_val, True
            else:
                return min_val, max_val, False

        if not root:
            return False
        return dfs(root)[2]


class Solution_Top_Down: #Time Complexity: O(N)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_value, max_value):
            if node.val >= max_value or node.val <= min_value:
                return False
            is_left_valid = True
            is_right_valid = True
            if node.left:
                is_left_valid = dfs(node.left, min_value, node.val)
            if node.right:
                is_right_valid = dfs(node.right, node.val, max_value)
            return is_left_valid and is_right_valid

        if root is None:
            return False
        ans = dfs(root, -math.inf, math.inf)
        return ans

    def isValidBST_Bottomup(self, root: Optional[TreeNode]) -> bool:#TODOO
        def dfs(node):
            smallest = largest = node.val
            if node.left is None and node.right is None:
                return (True,smallest,largest)

            if node.left:
                left_subtree = dfs(node.left)
            if node.right:
                right_subtree = dfs(node.right)
            if left_subtree[0] == False or right_subtree[0] == False:
                return (False,smallest,largest)
            if node.val > left_subtree[2] or node.val < right_subtree[1]:
                return (False, smallest, largest)

            return (False, left_subtree[1], right_subtree[2])

        if root is None:
            return False
        ans = dfs(root)
        return ans[0]
