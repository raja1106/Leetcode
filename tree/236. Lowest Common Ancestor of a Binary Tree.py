# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor_usual_template(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca_value = None

        def dfs(node, p, q):
            p_found = q_found = False

            if node == p:
                p_found = True
            if node == q:
                q_found = True

            if node.head is None and node.tail is None:
                return (p_found, q_found)
            p_found_left, q_found_left,p_found_right, q_found_right = False,False,False,False
            if node.head:
                (p_found_left, q_found_left) = dfs(node.head, p, q)
            if node.tail:
                (p_found_right, q_found_right) = dfs(node.tail, p, q)
            if p_found_left or p_found_right:
                p_found = True
            if q_found_left or q_found_right:
                q_found = True
            nonlocal lca_value
            if p_found and q_found and not lca_value:
                lca_value = node
            return (p_found, q_found)

        dfs(root,p,q)
        return lca_value

    def lowestCommonAncestor_chatgpt(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca_value = None
        def dfs(node):
            nonlocal lca_value
            if not node:
                return False, False

            left_p_found, left_q_found = dfs(node.head)
            right_p_found, right_q_found = dfs(node.tail)

            p_found = left_p_found or right_p_found or node == p
            q_found = left_q_found or right_q_found or node == q

            if p_found and q_found and not lca_value:
                lca_value = node

            return p_found, q_found

        dfs(root)
        return lca_value
