from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]

        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        row, col = 0, 0
        visited = set()

        visited.add((row, col))
        current = head
        while current:
            if result[0][0] == -1:
                result[0][0] = current.val
                current = current.next
                if not current:
                    break

            current_dirction = direction[i % 4]
            dr = current_dirction[0]
            dc = current_dirction[1]
            if 0 <= row + dr < m and 0 <= col + dc < n and (row + dr, col + dc) not in visited:
                row = row + dr
                col = col + dc
                result[row][col] = current.val
                visited.add((row, col))
                current = current.next
            else:
                i += 1

        return result