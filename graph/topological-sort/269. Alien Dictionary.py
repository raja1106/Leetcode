from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Step 1: Create a graph and an in-degree dictionary
        graph = defaultdict(set)
        # Python processes the for loops from left to right. {key: value for outer_loop for inner_loop}
        in_degree = {char: 0 for word in words for char in word}

        # Step 2: Build the graph and calculate in-degrees
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            # Check for invalid order: prefix case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""
            # Compare characters of the two words
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in graph[char1]:
                        graph[char1].add(char2)
                        in_degree[char2] += 1
                    break  # Only the first differing character determines the order

        # Step 3: Perform topological sort using BFS (Kahn's algorithm)
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)

            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check for cycle (invalid order)
        if len(order) != len(in_degree):
            return ""

        # Step 5: Return the lexicographical order
        return ''.join(order)
