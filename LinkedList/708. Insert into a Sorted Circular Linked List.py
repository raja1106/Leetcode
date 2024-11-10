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
