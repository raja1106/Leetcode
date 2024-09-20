from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Build the graph
        graph = defaultdict(list)  # adjacency list graph
        in_degree = defaultdict(int)  # count of incoming edges

        # Initialize in_degree for each character
        for word in words:
            for char in word:
                in_degree[char] = 0

        # Step 2: Add edges and update in-degrees
        for i in range(len(words) - 1):
            first, second = words[i], words[i + 1]
            min_len = min(len(first), len(second))

            # Check for invalid case where prefix is longer than the word after it
            if len(first) > len(second) and first[:min_len] == second[:min_len]:
                return ""

            # Compare characters and build the graph
            for j in range(min_len):
                if first[j] != second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].append(second[j])
                        in_degree[second[j]] += 1
                    break  # Stop after the first different character

        # Step 3: Topological sort using BFS (Kahn’s algorithm)
        # Initialize queue with nodes having zero in-degree
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        alien_order = []

        while queue:
            current_char = queue.popleft()
            alien_order.append(current_char)

            # Decrease the in-degree of the neighbors
            for neighbor in graph[current_char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: If we processed all characters, return the result
        if len(alien_order) == len(in_degree):
            return ''.join(alien_order)
        else:
            return ""  # There exists a cycle, hence no valid ordering
