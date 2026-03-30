from collections import Counter, deque
from heapq import heapify, heappop, heappush
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        char_frequency = Counter(s)

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
'''
'''

class Solution_2026:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        # Max-heap: use negative frequency
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        queue = deque()  # (neg_count, char, release_index)
        result = []

        while max_heap:
            neg_count, char = heapq.heappop(max_heap)
            result.append(char)
            # Schedule this char to be available again after k positions
            queue.append((neg_count + 1, char, len(result) - 1 + k))
            #              ^^ +1 because neg_count is negative, so +1 = decrement freq

            # Release characters whose cooldown has expired
            if queue and queue[0][2] <= len(result):
                released = queue.popleft()
                if released[0] < 0:  # still has remaining occurrences.. You can do this check before appending to queue as well
                    heapq.heappush(max_heap, (released[0], released[1]))

        if len(result) != len(s):
            return ""
        return "".join(result)

    #Another version
    def rearrange_string_k_apart(s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        max_heap = [(-count, ch) for ch, count in freq.items()]
        heapify(max_heap)

        cooldown = deque()
        result = []

        while max_heap:
            neg_count, ch = heappop(max_heap)
            result.append(ch)
            cooldown.append((neg_count + 1, ch))

            if len(cooldown) >= k:
                neg_cnt, prev_ch = cooldown.popleft()
                if neg_cnt < 0:  # still has remaining count You can do this check only here unlike the above approach
                    heappush(max_heap, (neg_cnt, prev_ch))

        if len(result) != len(s):
            return ""
        return "".join(result)
