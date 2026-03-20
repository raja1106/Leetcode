from heapq import heappush_max,heappop_max
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        barcodes_counter = Counter(barcodes)
        max_heap = []
        result = []
        for value,count in barcodes_counter.items():
            heappush_max(max_heap,(count,value))
        last_value,last_count = None,None
        while max_heap:
            count,value = heappop_max(max_heap)
            result.append(value)
            if last_value is not None:
                heappush_max(max_heap,(last_count,last_value))
            if count > 1:
                last_count, last_value = count-1,value
            else:
                last_value,last_count = None,None
        return result



'''

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        n = len(barcodes)
        maxheap = []
        for key, freq in counter.items():
            heapq.heappush(maxheap, (-freq, key))
        # i = 0

        res = []
        prevChar, prevCnt = "", 0
        while maxheap:
            negFreq, key = heapq.heappop(maxheap)
            posFreq = -negFreq
            res.append(key)

            if prevCnt > 0:
                heapq.heappush(maxheap, (-prevCnt, prevChar))

            posFreq -= 1
            prevCnt, prevChar = posFreq, key
        return res
'''