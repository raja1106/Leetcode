from collections import defaultdict, deque
from typing import List
'''
Given a Directed Acyclic Graph of N vertices from 0 to N-1 and M edges 
and a 2D Integer array edges, where there is a directed edge from vertex edge[i][0] to vertex edge[i][1] 
with a distance of edge[i][2] for all i.

Find the shortest path from source vertex to all the vertices and if it is impossible to reach any vertex,
 then return -1 for that vertex. The source vertex is assumed to be 0.

Example 1:


Input: N = 4, M = 2 edge = [[0,1,2],[0,2,1]]

Output: 0 2 1 -1

Explanation:

Shortest path from 0 to 1 is 0->1 with edge weight 2. 

Shortest path from 0 to 2 is 0->2 with edge weight 1.

There is no way we can reach 3, so it's -1 for 3.
'''

class Solution:
    def shortestPath(self, N: int, M: int, edges: List[List[int]]) -> List[int]:

        # Edge case
        if N == 0:
            return []

        # Build the graph and calculate in-degrees
        graph = defaultdict(list)
        in_degree = defaultdict(int)

        # edge = [src, dst, weight]
        for src, dst, weight in edges:
            graph[src].append((dst, weight))
            in_degree[dst] += 1

        # Initialize queue with all nodes having in-degree 0
        queue = deque([i for i in range(N) if in_degree[i] == 0])

        topological_order = []

        # Step 1: Find topological order using Kahn's BFS
        while queue:
            node = queue.popleft()
            topological_order.append(node)

            for neighbor, weight in graph[node]:
                in_degree[neighbor] -= 1

                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 2: Initialize distances
        distance = [float('inf')] * N

        # Source node is 0
        distance[0] = 0

        # Step 3: Process nodes in topological order
        for node in topological_order:

            # If node is unreachable from source 0, skip it
            if distance[node] == float('inf'):
                continue

            # Relax all outgoing edges
            for neighbor, weight in graph[node]:

                new_distance = distance[node] + weight

                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance

        # Step 4: Convert unreachable nodes from infinity to -1
        for i in range(N):
            if distance[i] == float('inf'):
                distance[i] = -1

        return distance