class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src,dst,weight in times:
            graph[src].append((dst,weight))
        # Priority queue to store the minimum distance node
        pq = [(0, k)]
        # Distance array to store the minimum distance to each node
        dist = [float('inf')] * (n+1)
        dist[0] = 0
        # Start from the source node
        dist[k] = 0
        while pq:
        # Get the node with the minimum distance
            current_distance, current_node = heapq.heappop(pq)
        # Traverse all the adjacent nodes
            for neighbour, weight in graph[current_node]:
            # Relaxation step
                if current_distance + weight < dist[neighbour]:
                    dist[neighbour] = current_distance + weight
                    heapq.heappush(pq, (dist[neighbour], neighbour))
        return -1 if max(dist) == float('inf') else max(dist)