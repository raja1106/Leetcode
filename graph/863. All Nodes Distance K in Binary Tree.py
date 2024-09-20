from collections import deque, defaultdict
from typing import List
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Create parent-child relationships using DFS
        parent = {}
        def dfs(node):
            if not node:
                return
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)

        dfs(root)

        # Step 2: BFS to find all nodes at distance K
        queue = deque([(target, 0)])
        visited = set([target])

        while queue:
            current_node, current_distance = queue[0]
            if current_distance == k:
                break

            current_node, current_distance = queue.popleft()

            # Visit left child
            if current_node.left and current_node.left not in visited:
                visited.add(current_node.left)
                queue.append((current_node.left, current_distance + 1))

            # Visit right child
            if current_node.right and current_node.right not in visited:
                visited.add(current_node.right)
                queue.append((current_node.right, current_distance + 1))

            # Visit parent node
            if current_node in parent and parent[current_node] not in visited:
                visited.add(parent[current_node])
                queue.append((parent[current_node], current_distance + 1))

        # Collect result for nodes at distance K
        result = [node.val for node, distance in queue]
        return result


import collections
from typing import List


class Solution_Using_Graph:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Initialize graph to store the adjacency list of the tree.
        graph = collections.defaultdict(list)

        # Recursively build an undirected graph from the binary tree.
        def build_graph(current_node, parent_node):
            if current_node:
                if parent_node:
                    graph[current_node.val].append(parent_node.val)
                    graph[parent_node.val].append(current_node.val)

                # Recur for children of the current node
                build_graph(current_node.left, current_node)
                build_graph(current_node.right, current_node)

        # Build the graph from the binary tree
        build_graph(root, None)

        # List to store the result
        result = []

        # Initialize a set to track visited nodes
        visited = set([target.val])

        # BFS queue initialized with the target node and distance 0
        queue = collections.deque([(target.val, 0)])

        while queue:
            node, distance = queue.popleft()

            # If the current node is at the required distance, add to result
            if distance == k:
                result.append(node)
                continue

            # Explore all neighbors (connected nodes in the graph)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    queue.append((neighbor, distance + 1))  # Enqueue with incremented distance

        return result
