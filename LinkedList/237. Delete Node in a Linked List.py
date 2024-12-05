class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Key Observations:

1. No Head Reference: Since you are not given the head of the linked list, you cannot traverse the list.
2. Delete Without Traversal: To delete the given node, you need to modify its content and links.

Core Idea:
To "delete" the node:

Copy the data from the next node into the current node.
Update the next pointer of the current node to skip the next node.
This approach effectively removes the next node while keeping the current node intact. 
Since the next node's data is now copied to the current node, it "looks like" the current node is deleted.
"""
def deleteNode(node):
    # Copy the value of the next node into the current node
    node.val = node.next.val
    # Skip the next node by updating the current node's next pointer
    node.next = node.next.next
