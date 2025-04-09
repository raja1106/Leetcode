class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly-linked list.

        Args:
            head (Optional[ListNode]): The head node of the linked list.

        Returns:
            Optional[ListNode]: The new head node of the reversed linked list.
        """
        # Initialize 'prev' to None. As the list is reversed, 'prev' will eventually point to
        # the new head of the reversed list, while the original head becomes the new tail.
        prev = None

        # Start with the current node at the head of the list.
        current = head

        # Traverse through the list until we reach the end.
        while current:
            # Store the next node because the link will be broken.
            next_node = current.next
            # Reverse the pointer of the current node to point to the previous node.
            current.next = prev
            # Move 'prev' one step forward to the current node.
            prev = current
            # Proceed to the next node using the stored next_node.
            current = next_node

        # At this point, 'prev' points to the new head of the reversed list.
        return prev


class Solution_Bottom_Up:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        # This variable will hold the new head of the reversed list.
        global_head = None

        def helper(node: ListNode) -> ListNode:
            if node is None:
                return None
            """
            Recursively travels to the end of the list and then reverses the pointers
            as the call stack unwinds.

            Args:
                node (ListNode): The current node in the recursion.

            Returns:
                ListNode: The current node after reversal (acting as the tail of the reversed sublist).
            """
            nonlocal global_head  # Allows us to modify the global_head variable defined in the outer function.

            # Base Case: If this is the last node, set it as the new head.
            if node.next is None:
                global_head = node
                return node

            # Recursive Case: Internal Node
            next_node = node.next
            node.next = None
            tail = helper(next_node)
            tail.next = node
            return node  # new tail

        # Start the recursion with the head node.
        helper(head)

        # global_head now points to the new head of the reversed list.
        return global_head


class Solution_Top_Down_Approach:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        # This variable will hold the new head of the reversed list.
        global_head = None

        def helper(node: ListNode, prev: ListNode) -> None:
            nonlocal global_head  # Allows us to modify the global_head variable defined in the outer function.
            # Base Case: If this is the last node, set it as the global head.
            if node.next is None:
                node.next = prev
                global_head = node
                return  # return as None as this is Top-Down approach
            # Recursive Case: Internal Node
            next_node = node.next
            node.next = prev
            helper(next_node, node)

        # Start the recursion with the head node and prev node.
        helper(head, None)
        # global_head now points to the new head of the reversed list.
        return global_head
