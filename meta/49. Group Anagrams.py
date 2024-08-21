from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary to store the groups of anagrams
        anagrams = defaultdict(list)

        for s in strs:
            # Sort each string to get a common key for all its anagrams
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            anagrams[sorted_str].append(s)

        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())
