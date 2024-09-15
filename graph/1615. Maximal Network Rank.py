class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        def build_graph():
            for src, dst in roads:
                graph[src].append(dst)
                graph[dst].append(src)

        build_graph()
        maximal_network_rank = 0
        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                current_rank = len(graph[node1]) + len(graph[node2])
                if node2 in graph[node1]:
                    current_rank -= 1
                maximal_network_rank = max(maximal_network_rank, current_rank)

        return maximal_network_rank

