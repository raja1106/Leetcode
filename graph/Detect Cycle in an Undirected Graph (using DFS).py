from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)

    def dfs(self, v, visited, parent):
        visited[v] = True

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                if self.dfs(neighbor, visited, v):
                    return True
            elif neighbor != parent:
                return True
        return False
    def is_cyclic(self):
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.dfs(i, visited, -1):
                    return True
        return False


# Example usage:
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(1, 3)
g.add_edge(3, 4)

if g.is_cyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle")
