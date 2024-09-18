class Solution:
    def alienOrder(self, words: List[str]) -> str:

        graph = defaultdict(list)

        def compare(i, j):
            # Compare two words and add an edge for the first difference
            for a, b in zip(words[i], words[j]):
                if a != b:
                    graph[a].append(b)
                    return True
            # If no difference was found, check if the first word is longer than the second
            return len(words[i]) <= len(words[j])

        # Initialize the graph with all unique characters
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = []
        # Compare adjacent words to build the graph
        num_words = len(words)
        for i in range(num_words - 1):
            if not compare(i, i + 1):
                return ""
        visited = set()
        stack = []
        rec_stack = set()

        def has_cycle(u):
            visited.add(u)
            rec_stack.add(u)
            for neighbor in graph[u]:
                if neighbor not in visited:
                    if has_cycle(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True
            stack.append(u)
            rec_stack.remove(u)
            return False

        # Perform DFS on each node
        for u in graph:
            if u not in visited:
                if has_cycle(u):
                    return ""

        # Return the topologically sorted characters
        return "".join(stack[::-1])
