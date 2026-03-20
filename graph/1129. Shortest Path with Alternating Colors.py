from collections import defaultdict, deque
from collections import deque, defaultdict
from typing import List

from collections import defaultdict, deque
from typing import List

class Solution_Best:
    def shortestAlternatingPaths( self,n: int,redEdges: List[List[int]],blueEdges: List[List[int]]) -> List[int]:

        # Color constants
        BLUE = 0
        RED = 1

        # Separate adjacency lists for each edge color
        red_graph = defaultdict(list)
        blue_graph = defaultdict(list)

        for src, dst in redEdges:
            red_graph[src].append(dst)
        for src, dst in blueEdges:
            blue_graph[src].append(dst)

        # result[i] = shortest alternating-color path distance from node 0 to node i
        # -1 means node i is unreachable
        result = [-1] * n
        result[0] = 0

        # BFS state: (node, distance, prev_color)
        # We enqueue node 0 twice — once assuming the first edge will be RED,
        # once assuming BLUE, since either is valid as a starting color
        queue = deque([
            (0, 0, RED),  # last color was RED, so next edge must be BLUE
            (0, 0, BLUE)  # last color was BLUE, so next edge must be RED
        ])

        # Track visited (node, color) pairs to avoid revisiting the same
        # node arrived at via the same color (prevents cycles)
        visited = {
            (0, RED),
            (0, BLUE)
        }

        while queue:
            node, distance, prev_color = queue.popleft()

            # Next edge must alternate: if we arrived via RED, go BLUE and vice versa
            if prev_color == RED:
                next_neighbors = blue_graph[node]
                next_color = BLUE
            else:
                next_neighbors = red_graph[node]
                next_color = RED

            for neighbor in next_neighbors:
                # Skip if we've already reached this neighbor via the same color
                # (same color = same state, and BFS already found the shortest path)
                if (neighbor, next_color) in visited:
                    continue

                visited.add((neighbor, next_color))
                queue.append((neighbor, distance + 1, next_color))

                # First time reaching this neighbor = shortest distance (BFS guarantee)
                if result[neighbor] == -1:
                    result[neighbor] = distance + 1

        return result


class Solution_2026:
    def shortestAlternatingPaths(self, n: int,
                                 redEdges: List[List[int]],
                                 blueEdges: List[List[int]]
                                 ) -> List[int]:

        BLUE, RED = 0, 1  # BLUE=0, RED=1

        # Build adjacency list: adj[u] = [(v, color)]
        adj = defaultdict(list)
        for u, v in redEdges:
            adj[u].append((v, RED))
        for u, v in blueEdges:
            adj[u].append((v, BLUE))
        # dist[i] = shortest alternating path from 0 to i
        dist = [-1] * n
        dist[0] = 0
        # State: (node, last_color_used)
        # Start with both colors since first edge from node 0 can be either color
        queue = deque()
        queue.append((0, RED))  # last color was RED, so next edge must be BLUE
        queue.append((0, BLUE))  # last color was BLUE, so next edge must be RED

        visited = {(0, RED), (0, BLUE)}

        steps = 0  # current BFS level (distance from node 0)

        while queue:
            steps += 1
            for _ in range(len(queue)):  # process all nodes at current distance level
                node, last_color = queue.popleft()

                for neighbor, edge_color in adj[node]:
                    # Must ALTERNATE: skip if edge color is same as last used color
                    if edge_color == last_color:
                        continue

                    if (neighbor, edge_color) not in visited:
                        visited.add((neighbor, edge_color))

                        # Only update dist on first visit (BFS guarantees shortest path)
                        if dist[neighbor] == -1:
                            dist[neighbor] = steps

                        queue.append((neighbor, edge_color))

        return dist
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        # Create adjacency lists for red and blue edges
        graph = [defaultdict(list) for _ in range(2)]
        for src, dst in redEdges:
            graph[0][src].append(dst)
        for src, dst in blueEdges:
            graph[1][src].append(dst)

        # Initialize distances: res[0] for red, res[1] for blue
        res = [[float('inf')] * n for _ in range(2)]
        res[0][0] = res[1][0] = 0  # Distance to start node is 0 for both colors

        # BFS queue: (node, color), where color is 0 (red) or 1 (blue)
        queue = deque([(0, 0), (0, 1)])  # Start with both red and blue edges from node 0

        while queue:
            node, color = queue.popleft()
            next_color = 1 - color  # Alternate color
            for neighbor in graph[next_color][node]:
                if res[next_color][neighbor] == float('inf'):
                    res[next_color][neighbor] = res[color][node] + 1
                    queue.append((neighbor, next_color))

        # Build the final answer
        answer = []
        for i in range(n):
            shortest = min(res[0][i], res[1][i])
            answer.append(shortest if shortest != float('inf') else -1)

        return answer
