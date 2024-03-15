from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        char_frequency = Counter(s)
        max_freq = max(char_frequency.values())

        if max_freq > (len(s) + 1) // 2:
            return ''

        result = []
        '''
        max_heap = []
        for k, v in char_frequency.items():
            heapq.heappush(max_heap, [-v, k])
         But below approach is better approach   
        '''
        max_heap = [[-freq, char] for char, freq in char_frequency.items()]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first_max = heapq.heappop(max_heap)
            first_max[0] += 1
            second_max = heapq.heappop(max_heap)
            second_max[0] += 1
            result.append(first_max[1])
            result.append(second_max[1])

            if first_max[0] != 0:
                heapq.heappush(max_heap, first_max)

            if second_max[0] != 0:
                heapq.heappush(max_heap, second_max)

        if max_heap:
            last_element = heapq.heappop(max_heap)
            if -1 * last_element[0] > 1:
                return ''
            else:
                result.append(last_element[1])

        return ''.join(result)


    def reorganizeString_lc(self, s: str) -> str:
        ans = []
        # Min heap ordered by character counts, so we will use
        # negative values for count
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(pq)

        while pq:
            count_first, char_first = heapq.heappop(pq)
            if not ans or char_first != ans[-1]:
                ans.append(char_first)
                if count_first + 1 != 0:
                    heapq.heappush(pq, (count_first + 1, char_first))
            else:
                if not pq: return ''
                count_second, char_second = heapq.heappop(pq)
                ans.append(char_second)
                if count_second + 1 != 0:
                    heapq.heappush(pq, (count_second + 1, char_second))
                heapq.heappush(pq, (count_first, char_first))

        return ''.join(ans)

obj =Solution()
print(obj.reorganizeString('aab'))
