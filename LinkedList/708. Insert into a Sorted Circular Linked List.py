class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)

        # Case 1: If the list is empty, create a new node that points to itself and return it
        if not head:
            new_node.next = new_node
            return new_node

        # Initialize pointers
        prev, current = head, head.next
        inserted = False  # Flag to check if insertion was done

        while True:
            # Case 2: Normal insertion within sorted values
            if prev.val <= insertVal <= current.val:
                inserted = True

            # Case 3: Insertion at the boundary (smallest or largest)
            elif prev.val > current.val:
                # Insert either as the largest or smallest value in the wrap-around
                if insertVal >= prev.val or insertVal <= current.val:
                    inserted = True

            # Insert the new node if any condition above was met
            if inserted:
                prev.next = new_node
                new_node.next = current
                return head

            # Move to the next pair of nodes
            prev, current = current, current.next

            # Case 4: Full circle traversal without insertion, list with uniform values
            if prev == head:
                prev.next = new_node
                new_node.next = current
                return head


class Solution_April_2025:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """
        Inserts a new node with value 'insertVal' into a cyclic sorted linked list.
        Returns the head of the modified list.
        """
        new_node = Node(insertVal)

        # If the list is empty, create a new cyclic list.
        if not head:
            new_node.next = new_node
            return new_node

        # If the list has only one node, insert the new node after head.
        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head

        # Use two pointers to traverse the list.
        prev, current = head, head.next
        while True:
            # Case 1: Normal insertion point between two sorted nodes.
            if prev.val <= insertVal <= current.val:
                break

            # Case 2: At the turning point where the list wraps around.
            if prev.val > current.val:
                # Insert if the new value is either greater than the max or less than the min.
                if insertVal > prev.val or insertVal < current.val:
                    break

            # Move to the next pair of nodes.
            prev, current = current, current.next

            # If we've made a full loop, insert the new node here.
            if prev == head:
                break

        # Insert the new node between prev and current.
        new_node.next = prev.next
        prev.next = new_node
        return head


class Solution_Find_Minimum_Approach:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """
        Inserts a new node with the given insertVal into a cyclic sorted linked list
        using a two-pass approach with only a `prev` pointer:
          1. First Pass: Locate the maximum node (where prev.val > prev.next.val).
             The node following the maximum node is the minimum node.
          2. Second Pass: Starting from the minimum node, traverse the list using a
             single `prev` pointer to find the correct insertion point.
        """
        new_node = Node(insertVal)

        # Case 1: Empty list.
        if not head:
            new_node.next = new_node
            return new_node

        # Case 2: List with one node.
        if head.next == head:
            head.next = new_node
            new_node.next = head
            return head

        # --- First Pass: Find the turning point ---
        # Using `prev` pointer, locate the maximum node in the list.
        prev = head
        while True:
            # When the current node is greater than the next node,
            # we've found the maximum.
            if prev.val > prev.next.val:
                break
            prev = prev.next
            # If we've looped through the entire list, it means the list
            # has uniform values.
            if prev == head:
                break

        # The minimum node is right after the maximum node.
        min_node = prev.next

        # --- Second Pass: Find the correct insertion position ---
        # Start from the minimum node and use the `prev` pointer.
        prev = min_node
        while True:
            # Normal case: insert if insertVal fits between two nodes.
            if prev.val <= insertVal <= prev.next.val:
                break
            prev = prev.next
            # If we've made a full cycle without finding an appropriate spot,
            # break out and insert at the current position.
            if prev == min_node:
                break

        # Insert the new node between `prev` and `prev.next`.
        new_node.next = prev.next
        prev.next = new_node

        return head
