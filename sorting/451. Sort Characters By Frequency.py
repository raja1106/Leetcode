import heapq
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequency = Counter(s)

        sorted_characters = sorted(char_frequency.items(), key=lambda item: -item[1]) # <class 'list'> this is list of Tuples

        frequency_sorted_string = ''.join(character * frequency for character, frequency in sorted_characters)
        return frequency_sorted_string

#Using max heap..  We are using max heap instead of min heap as there is no requirement of top k items here

    def frequencySortUsingMaxheap(self, s: str) -> str:
        char_frequency = Counter(s)
        max_heap =[(-freq,char) for char,freq in char_frequency.items()]
        heapify(max_heap)
        result=[]
        while max_heap:
            freq,char = heapq.heappop(max_heap)
            result.append(char * -freq)

        return ''.join(result)




obj=Solution()
print(obj.frequencySort('etststreeet'))
