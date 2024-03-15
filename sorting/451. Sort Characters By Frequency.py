from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        char_frequency = Counter(s)
        sorted_characters = sorted(char_frequency.items(), key=lambda item: -item[1])
        frequency_sorted_string = ''.join(character * frequency for character, frequency in sorted_characters)
        return frequency_sorted_string

#TODOO using min heap




obj=Solution()
obj.frequencySort('ststreet')
