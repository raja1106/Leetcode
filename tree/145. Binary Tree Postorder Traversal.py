# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                result.append(node.val)
                stack[-1] = (node, "departure")

            # 4) Zone = "departure": we pop the stack
            else:  # zone == "departure"
                stack.pop()

        return result