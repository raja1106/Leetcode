from collections import defaultdict
import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        # Build the graph where each edge has a probability (weight)
        for i, (src, dst) in enumerate(edges):
            weight = succProb[i]
            graph[src].append((dst, weight))
            graph[dst].append((src, weight))

        # Priority queue to store nodes with their max probability (using -1 to simulate max-heap behavior)
        pq = [(-1, start_node)]  # (negative probability, node)

        # Array to store the maximum probability to each node
        probabilities = [-1] * n
        probabilities[start_node] = 1

        while pq:
            # Pop the node with the current highest probability (simulated max-heap)
            current_probability, current_node = heapq.heappop(pq)
            current_probability *= -1  # Convert back to positive probability

            # Traverse all the adjacent nodes
            for neighbor, weight in graph[current_node]:
                new_probability = current_probability * weight
                if new_probability > probabilities[neighbor]:
                    probabilities[neighbor] = new_probability
                    heapq.heappush(pq, (-new_probability, neighbor))

        # Return 0 if there's no valid path to the end_node, otherwise the max probability
        return 0 if probabilities[end_node] == -1 else probabilities[end_node]
