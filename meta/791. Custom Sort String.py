from heapq import heappush, heappop

from collections import Counter

class Solution_Best:
    def customSortString(self, order: str, s: str) -> str:
        # Create a frequency table using Counter
        freq = Counter(s)

        # Build the result by appending characters in the order
        result = [letter * freq.pop(letter) for letter in order if letter in freq]

        # Append the remaining characters from `s` that were not in `order`
        result.extend([letter * count for letter, count in freq.items()])

        # Join and return the result as a string
        return ''.join(result)

class Solution_Efficient_2:

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


class Solution_Efficient_3:
    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary to store the order of each character
        order_index = {c: i for i, c in enumerate(order)}

        # Sort the characters in 's' based on their order in 'order'
        sorted_s = sorted(s, key=lambda x: order_index.get(x, -1))

        return ''.join(sorted_s)
class Solution_Not_Efficient:
    def customSortString(self, order: str, s: str) -> str:
        # Convert string `s` into a list for sorting
        result = list(s)  # O(N), where N is the length of string `s`

        # Define the custom comparator
        result.sort(key=lambda c: order.index(c) if c in order else len(order) + 1)
        # Time complexity: O(N * M), where N is the length of string `s` and M is the length of string `order`.

        # Convert the sorted list back into a string and return it
        return ''.join(result)  # O(N)
