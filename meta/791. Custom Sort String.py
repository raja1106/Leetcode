from heapq import heappush, heappop
class Solution:

    # Both of the below approaches have O(nlogn) time complexity
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Create a dictionary to store the order of each character
        letter_order = {c: i for i, c in enumerate(order)}

        # Step 2: Initialize a min-heap
        min_heap = []

        # Step 3: Push elements of s into the heap based on their order in 'order'
        for ch in s:
            if ch in letter_order:
                heappush(min_heap, (letter_order[ch], ch))
            else:
                heappush(min_heap, (-1, ch))  # Characters not in 'order' get lowest priority

        # Step 4: Extract characters from the heap and form the result string
        result = [heappop(min_heap)[1] for _ in range(len(min_heap))]

        return ''.join(result)


class Solution_Efficient:
    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary to store the order of each character
        order_index = {c: i for i, c in enumerate(order)}

        # Sort the characters in 's' based on their order in 'order'
        sorted_s = sorted(s, key=lambda x: order_index.get(x, -1))

        return ''.join(sorted_s)
