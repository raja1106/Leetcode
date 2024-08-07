# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Dictionary to keep track of copied nodes
        visited = {}

        def dfs(node: 'Node') -> 'Node':
            if node in visited:
                return visited[node]

            # Clone the node
            clone = Node(node.val)
            visited[node] = clone

            # Clone all the neighbors recursively
            if node.neighbors:
                clone.neighbors = [dfs(neighbor) for neighbor in node.neighbors]

            return clone

        # Start DFS from the input node
        return dfs(node)
