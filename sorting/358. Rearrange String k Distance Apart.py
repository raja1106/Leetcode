from collections import Counter, deque
from heapq import heapify, heappop, heappush
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        char_frequency = Counter(s)
        max_freq = max(char_frequency.values())

        if k == 0:
            return s

        result = []
        frequency_heap = [[-freq, char] for char,freq in char_frequency.items()]
        heapq.heapify(frequency_heap)

        while len(frequency_heap) >= k:
            temp = []
            for i in range(k):
                element = heapq.heappop(frequency_heap)
                result.append(element[1])
                element[0] += 1
                if element[0] != 0:
                    temp.append(element)
            frequency_heap.extend(temp)
            heapq.heapify(frequency_heap)

        while frequency_heap:
            element = heapq.heappop(frequency_heap)
            if element[0] != -1:
                return ''
            else:
                result.append(element[1])

        return ''.join(result)

    def rearrangeString_monst(self, s: str, k: int) -> str:
        # If k is 0 or 1, no rearrangement is needed, just return the original string.
        if k <= 1:
            return s

        # Create a max heap based on the frequency of characters in the string
        # where the most frequent character is at the top.
        # Negate the frequency counts as Python has a min-heap by default.
        frequency_heap = [(-frequency, char) for char, frequency in Counter(s).items()]
        heapify(frequency_heap)

        # Use a queue to keep track of characters that have been used, to maintain
        # the distance of 'k' between the same characters.
        wait_queue = deque()

        # This list will contain the rearranged characters.
        rearranged_string = []

        # Process the heap until all characters are rearranged.
        while frequency_heap:
            # Pop the character with the highest frequency.
            frequency, char = heappop(frequency_heap)
            # Reverse the negation to get the positive frequency count.
            frequency = -frequency

            # Append the character to the result.
            rearranged_string.append(char)

            # Record the character in the queue with its updated frequency,
            # to be pushed back into the heap when it's allowed (after 'k' placements).
            wait_queue.append((frequency - 1, char))

            # If the waiting queue has 'k' elements, it's time to add an element back
            # to the heap (if it still has a non-zero frequency).
            if len(wait_queue) == k:
                wait_frequency, wait_char = wait_queue.popleft()
                if wait_frequency > 0:
                    heappush(frequency_heap, (-wait_frequency, wait_char))

        # If the length of the rearranged string equals the original string length,
        # return the rearranged string as it's valid. Otherwise, return an empty string.
        return "".join(rearranged_string) if len(rearranged_string) == len(s) else ""