from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array
        self.rank = [0] * size  # Initialize rank array

    def find(self, x):
        #return root as usual after doing path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)  # Find root of x
        rootY = self.find(y)  # Find root of y
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX  # Union by rank
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY  # Union by rank
            else:
                self.parent[rootY] = rootX  # Union by rank
                self.rank[rootX] += 1  # Increment rank if ranks are equal

class Solution:
    def possibleBipartition(self, n, dislikes):
        from collections import defaultdict
        adj = defaultdict(list)  # Create adjacency list for dislikes
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        uf = UnionFind(n + 1)  # Initialize UnionFind structure
        for node in range(1, n + 1):
            if not adj[node]:
                continue  # Skip if the node has no dislikes
            for neighbor in adj[node]:
                if uf.find(node) == uf.find(neighbor):
                    return False  # If they are in the same set, return false
                uf.union(adj[node][0], neighbor)  # Union all neighbors into the same set as the first neighbor
        return True  # If no conflicts, return true

# Test cases
sol = Solution()
print(sol.possibleBipartition(5, [[1, 2], [2, 3], [3, 4], [4, 5]]))  # true
print(sol.possibleBipartition(6, [[1, 2], [2, 4], [4, 6], [4, 5], [5, 6]]))  # false
print(sol.possibleBipartition(3, [[1, 2], [1, 3]]))  # true



class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:

        # Helper function to find the root of the set that element `x` belongs to.
        def find_root(x):
            while parent[x] != x:
                # Path compression: make each looked-at node point to the root
                parent[x] = find_root(parent[x])
            return parent[x]

        # Graph representation where key is a node and values are the nodes that are disliked by the key
        graph = defaultdict(list)
        for a, b in dislikes:
            # Since people are numbered from 1 to N, normalize to 0 to N-1 for zero-indexed arrays
            a, b = a - 1, b - 1
            # Add each to the dislike list of the other
            graph[a].append(b)
            graph[b].append(a)

        # Initialize the parent array for disjoint-set union-find, each node is its own parent initially
        parent = list(range(n))

        # Process every person
        for i in range(n):
            # Check dislikes for person `i`
            for j in graph[i]:
                # If person `i` and one of the people who dislike `i` has the same root, partition is not possible
                if find_root(i) == find_root(j):
                    return False
                # Union operation: Connect the groups of the first disliked person to other disliked nodes' group
                parent[find_root(j)] = find_root(graph[i][0])

        # If no conflicts found, partitioning is possible
        return True

    def possibleBipartition_1(self, n: int, dislikes: List[List[int]]) -> bool:

        # Helper function to find the root of the set that element `x` belongs to (with path compression).
        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])  # Path compression
            return parent[x]

        # Union two sets containing elements `x` and `y`.
        def union(x, y):
            rootX = find_root(x)
            rootY = find_root(y)
            if rootX != rootY:
                parent[rootX] = rootY  # Union by assigning one root to the other

        # Graph representation where key is a node and values are the nodes disliked by the key
        graph = defaultdict(list)
        for a, b in dislikes:
            # Normalize indices from 1-based to 0-based for internal array indexing
            a, b = a - 1, b - 1
            graph[a].append(b)
            graph[b].append(a)

        # Initialize the parent array for disjoint-set union-find
        parent = list(range(n))

        # Traverse through each node and its dislikes
        for i in range(n):
            if i in graph:  # Only process nodes that have dislikes
                for j in graph[i]:
                    # If `i` and any node `j` it dislikes are in the same set, return False
                    if find_root(i) == find_root(j):
                        return False
                    # Union the first disliked node and the current disliked node
                    union(graph[i][0], j)

        # If no conflicts are found, bipartition is possible
        return True
