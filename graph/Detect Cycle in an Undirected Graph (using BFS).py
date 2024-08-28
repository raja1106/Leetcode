from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
    def add_edge(self, v, w):
        self.graph[v].append(w)
        self.graph[w].append(v)
    def bfs(self, v, visited):
        queue = deque([(v, -1)])  # (current node, parent node)
        visited[v] = True

        while queue:
            current, parent = queue.popleft()

            for neighbor in self.graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, current))
                elif neighbor != parent:
                    return True
        return False
    def is_cyclic(self):
        visited = [False] * self.V

        for i in range(self.V):
            if not visited[i]:
                if self.bfs(i, visited):
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
