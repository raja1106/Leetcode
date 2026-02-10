import heapq

class MaxStack_Two_Stack:
    def __init__(self):
        self.stack = []  # Main stack to store all elements
        self.max_stack = []  # Stack to store the maximum at each state

    def push(self, x: int) -> None:
        self.stack.append(x)
        # If max_stack is empty or x >= current max, push x.
        # Otherwise, push the current max again to keep stack sizes synced.
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self) -> int:
        self.max_stack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]
    #[5, 5, 2, 5, 1, 2]
    def popMax(self) -> int:
        target_max = self.max_stack[-1]
        buffer = []

        # We must find the actual max in the main stack.
        # Elements are moved to a buffer until the target_max is found.
        while self.top() != target_max:
            buffer.append(self.pop())

        # Remove the max element itself
        actual_max = self.pop()

        # Push the buffered elements back in their original order
        while buffer:
            self.push(buffer.pop())

        return actual_max
    def print_stack(self):
        return self.stack
class Node:
    def __init__(self, val, count, prev=None, next=None):
        self.val = val
        self.count = count
        self.prev = prev
        self.next = next


class MaxStack_Using_Linked_List:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_heap = []  # (val,count)
        self.removed_set = set()  # (val,idx) lazy deletion
        self.count = 0

    def push(self, x: int) -> None:
        self.count += 1
        count = self.count
        new_node = Node(x, count)
        prev_node = self.tail.prev
        # new_node = self.tail.prev
        new_node.prev = prev_node
        new_node.next = self.tail
        prev_node.next = new_node
        self.tail.prev = new_node
        heapq.heappush_max(self.max_heap, (x, count, new_node))

    def pop(self) -> int:
        removed_node = self.tail.prev  # 5
        self.tail.prev = removed_node.prev  # connecting tail with 1
        removed_node.prev.next = removed_node.next  # connecting  1 with tail node
        removed_val = removed_node.val
        removed_count = removed_node.count
        self.removed_set.add((removed_val, removed_count))
        self._clean_up()
        return removed_val

    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        return self.max_heap[0][0]

    def _clean_up(self):
        while self.max_heap:
            val = self.max_heap[0][0]
            count = self.max_heap[0][1]
            if (val, count) in self.removed_set:
                self.removed_set.remove((val, count))
                heapq.heappop_max(self.max_heap)
            else:
                break

    def popMax(self) -> int:
        max_element = heapq.heappop_max(self.max_heap)
        val = max_element[0]
        count = max_element[1]
        removed_node = max_element[2]
        next_node = removed_node.next
        prev_node = removed_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        removed_node.next = None
        removed_node.prev = None
        self._clean_up()
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
class MaxStack_Bruteforce_Approach:

    def __init__(self):
        self.st = []

    def push(self, x: int) -> None:
        self.st.append(x)

    def pop(self) -> int:
        return self.st.pop()

    def print_stack(self):
        return self.st

    def top(self) -> int:
        return self.st[-1]

    def peekMax(self) -> int:
        return max(self.st)

    def popMax(self) -> int:
        max_element = max(self.st)
        n = len(self.st)
        max_element_index = None
        for i in range(n - 1, -1, -1):
            if self.st[i] == max_element:
                max_element_index = i
                break
        # [5, 5, 1, 5, 1] j = 3,  [5, 5, 1, 1]
        j = max_element_index
        while j < n - 1:
            self.st[j] = self.st[j + 1]
            j += 1
        self.st.pop()
        return max_element

# Your MaxStack object will be instantiated and called as such:
obj = MaxStack_Two_Stack()
obj.push(5)
obj.push(5)
obj.push(2)
obj.push(5)
obj.push(1)
obj.push(2)
print(obj.print_stack())
print(f'obj.peekMax():{obj.peekMax()} ')
print(f'obj.popMax():{obj.popMax()} ')
print(obj.print_stack())
print(f'obj.popMax():{obj.popMax()} ')
print(f'obj.popMax():{obj.popMax()} ')
print(f'obj.popMax():{obj.popMax()} ')
print(f'obj.pop():{obj.pop()} ')
print(f'obj.popMax():{obj.popMax()} ')
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()