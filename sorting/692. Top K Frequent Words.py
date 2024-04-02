from typing import List
import heapq
class Solution:

    def topKFrequentUsingMaxHeap(self, words: List[str], k: int) -> List[str]: # This is preferable approach
        wordmap = Counter(words)
        max_heap = [(-freq, word) for word, freq in wordmap.items()]
        heapify(max_heap)
        return [heappop(max_heap)[1] for _ in range(k)] #T(n) : O(n)+O(k log n)

#Using Min Heap
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_frequency = Counter(words)
        min_heap = []
        result = []
        for word, freq in word_frequency.items():
            heapq.heappush(min_heap, Pair(freq, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [p.word for p in sorted(min_heap, reverse=True)]
class Pair:
        def __init__(self, freq, word):
            self.word = word
            self.freq = freq

        def __lt__(self, p):
            # Words with higher frequency and lower alphabetical order are in the
            # bottom of the heap because we'll pop words with lower frequency and
            # higher alphabetical order if the heap's size > k.
            return self.freq < p.freq or (self.freq == p.freq and self.word > p.word)





obj=Solution()
print(obj.topKFrequent(["i","love","leetcode","i","love","coding"],2))
#print(obj.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"],4))

