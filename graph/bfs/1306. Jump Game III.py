from collections import deque
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True

        queue = deque([start])
        visited = set([start])

        while queue:
            current_index = queue.popleft()

            if arr[current_index] == 0:
                return True

            # Check left and right neighbors
            for next_index in (current_index - arr[current_index], current_index + arr[current_index]):
                if 0 <= next_index < len(arr) and next_index not in visited:
                    visited.add(next_index)
                    queue.append(next_index)

        return False


class Solution_Naive_one:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        queue = deque()
        queue.append(start)
        visited = set()
        visited.add(start)
        while queue:
            current_node = queue.popleft()
            if arr[current_node] == 0:
                return True
            left_side_node = current_node - arr[current_node]
            right_side_node = current_node + arr[current_node]

            if 0 <= left_side_node < len(arr) and not left_side_node in visited:
                visited.add(left_side_node)
                queue.append(left_side_node)
            if 0 <= right_side_node < len(arr) and not right_side_node in visited:
                visited.add(right_side_node)
                queue.append(right_side_node)

        return False
