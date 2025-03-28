# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_Iterative:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        # Each stack entry is (node, zone)
        # zone can be None, "arrival", "interim", or "departure"
        stack = [(root, None)]

        while stack:
            node, zone = stack[-1]

            # 1) Zone = None: "arrival" to this node
            if zone is None:
                # Mark this node as "arrival"
                stack[-1] = (node, "arrival")
            # Pre-order means process the node value first
                result.append(node.val)
            # If there's a left child, push it onto the stack
                if node.left is not None:
                    stack.append((node.left, None))

            # 2) Zone = "arrival": we finished visiting left subtree
            # Now let's go to "interim"
            elif zone == "arrival":
                stack[-1] = (node, "interim")
                # Next, if there's a right child, push it
                if node.right is not None:
                    stack.append((node.right, None))

            # 3) Zone = "interim": left and right subtrees are done
            # Move to "departure" state
            elif zone == "interim":
                stack[-1] = (node, "departure")

            # 4) Zone = "departure": we pop the stack
            else:  # zone == "departure"
                stack.pop()

        return result


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        result = []
        stack = [(root, 0)]  # (node, state)

        while stack:
            node, state = stack.pop()

            if state == 0:
                result.append(node.val)# Pre: Visit before children
                if node.right:
                    stack.append((node.right, 0))# Right child
                if node.left:
                    stack.append((node.left, 0))# Left child

        return result
