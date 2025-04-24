class Node:
    def __init__(self, val: int, next: 'Node' = None, random: 'Node' = None):
        self.val = val
        self.next = next
        self.random = random
class Solution: # S(n) = O(1), T(n) = O(n)
    def copyRandomList(self, head: 'Node') -> 'Node':
        # If the original list is empty, return None.
        if not head:
            return None
        # Step 1: Create new nodes weaved within the original list
        current = head
        while current:
            # cloned_node is a copy of the current node without the random reference
            cloned_node = Node(current.val, current.next)
            current.next = cloned_node  # Insert the cloned node just after the current node
            current = cloned_node.next  # Move to the next original node
        # Step 2: Assign random pointers to the cloned nodes
        current = head
        while current:
            if current.random:
                # Set the cloned node's random to the cloned node of the original node's random
                current.next.random = current.random.next
            current = current.next.next  # Move two steps forward

        # Step 3: Detach the original and cloned list from each other
        original_current = head
        cloned_head = head.next
        while original_current:
            cloned_current = original_current.next
            original_current.next = cloned_current.next  # Fix the original list's next pointer
            # Fix the cloned list's next pointer, only if cloned_current has a next node
            if cloned_current.next:
                cloned_current.next = cloned_current.next.next
            # Move to the next original node
            original_current = original_current.next
        # Return the head of the cloned linked list
        return cloned_head


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution_More_Intuitive: # S(n) = O(n), T(n) = O(n)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Handle empty input
        if not head:
            return None

        # First pass: create new nodes and store the mapping from original to copy.
        node_map = {}  # Renamed from 'map' to avoid overshadowing built-in function.
        current = head
        dummy_head = Node(0)
        prev = dummy_head

        while current:
            new_node = Node(current.val)
            node_map[current] = new_node
            prev.next = new_node
            prev = new_node
            current = current.next

        # Second pass: assign random pointers for the new nodes.
        current_new = dummy_head.next
        current_old = head

        while current_new:
            if current_old.random is not None:
                current_new.random = node_map[current_old.random]
            current_old = current_old.next
            current_new = current_new.next

        return dummy_head.next
