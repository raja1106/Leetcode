from collections import defaultdict
import heapq
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        # Step 1: Build the graph
        graph = defaultdict(dict)

        for (u, v, w) in roads:
            graph[u][v] = w
            graph[v][u] = w

        # Step 2: Main Dijkstra function with a helper
        def dijkstra(start):
            dist = {i: float('inf') for i in range(n)}
            count = {i: 0 for i in range(n)}
            dist[start] = 0
            count[start] = 1

            queue = [(0, start)]  # Min-heap priority queue

            while queue:
                current_dist, u = heapq.heappop(queue)

                if current_dist > dist[u]:
                    continue

                for v in graph[u]:
                    alt = current_dist + graph[u][v]

                    if alt < dist[v]:
                        dist[v] = alt
                        count[v] = count[u]
                        heapq.heappush(queue, (alt, v))
                    elif alt == dist[v]:
                        count[v] = (count[v] + count[u]) % MOD

            return count[n - 1]

        # Use the helper function
        return dijkstra(0)

