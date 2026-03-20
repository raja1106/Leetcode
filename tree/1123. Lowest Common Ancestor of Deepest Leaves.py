from collections import deque, defaultdict
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        1. need to find deepest length nodes

        2. Can we traverse from that node to reach all deepest nodes
        List[nodes] in each level
        """
        if not root:
            return None

        queue = deque()
        queue.append((root, 0))
        depth_nodes = defaultdict(list)
        current_depth = 0

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node, depth = queue.popleft()
                depth_nodes[depth].append(node)

                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))

                current_depth = depth

        # Need to do bottom up DFS, POST Order DFS
        deepest_nodes = set(depth_nodes[current_depth])

        # bottom-up DFS:
        # returns how many deepest nodes exist in this subtree
        # sets self.ans when subtree contains all deepest nodes
        total_deepest = len(deepest_nodes)
        self.ans = None

        def dfs(node):
            if not node:
                return 0

            left_count = dfs(node.left)
            right_count = dfs(node.right)

            current = 1 if node in deepest_nodes else 0
            subtree_count = left_count + right_count + current

            # First (lowest) node whose subtree contains all deepest nodes
            if subtree_count == total_deepest and self.ans is None:
                self.ans = node

            return subtree_count

        dfs(root)
        return self.ans



from typing import Optional, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node: Optional[TreeNode]) -> Tuple[int, Optional[TreeNode]]:
            """
            Returns:
              (height_from_node, lca_of_deepest_leaves_in_this_subtree)

            height convention:
              None -> 0
              leaf -> 1
            """
            if not node:
                return 0, None

            left_depth, left_lca = dfs(node.left)
            right_depth, right_lca = dfs(node.right)

            if left_depth == right_depth:
                # deepest leaves are split across both sides (or node is leaf)
                return left_depth + 1, node
            elif left_depth > right_depth:
                return left_depth + 1, left_lca
            else:
                return right_depth + 1, right_lca

        return dfs(root)[1]