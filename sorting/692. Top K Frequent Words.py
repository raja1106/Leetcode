from typing import List
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        map={}

        for word in words:
            map[word] = map.get(word,0)+1

        min_heap = []
        result=[]
        print(map)
        for key,val in map.items():
            heapq.heappush(min_heap,(val,key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        print(heapq.heappop(min_heap))
        while min_heap:
            result.append(heapq.heappop(min_heap)[1])
        return result




    def topKFrequentUsingMaxHeap(self, words: List[str], k: int) -> List[str]:
        wordmap = Counter(words)
        max_heap = [(-freq, word) for word, freq in wordmap.items()]
        heapify(max_heap)

        return [heappop(max_heap)[1] for _ in range(k)]



obj=Solution()
print(obj.topKFrequent(["i","love","leetcode","i","love","coding"],2))
#print(obj.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))

