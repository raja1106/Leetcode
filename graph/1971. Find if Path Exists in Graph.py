from collections import defaultdict, deque
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Return True if the source and destination are the same without any edges
        if source == destination:
            return True

        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        # Perform BFS to find the path from source to destination
        queue = deque([source])
        visited = {source}

        while queue:
            current_node = queue.popleft()

            for neighbor in graph[current_node]:
                if neighbor == destination:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False
