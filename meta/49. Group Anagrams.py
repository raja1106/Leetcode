from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: #T(n) = O(n*mlogm)
        # Create a dictionary to store the groups of anagrams
        anagrams = defaultdict(list)

        for s in strs:
            # Sort each string to get a common key for all its anagrams
            sorted_str = ''.join(sorted(s))
            # Append the original string to the list corresponding to the sorted key
            anagrams[sorted_str].append(s)

        # Return the values of the dictionary as a list of lists
        return list(anagrams.values())


from collections import defaultdict
from typing import List


class Solution_Efficient: #T(n) = O(n · m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a dictionary to store grouped anagrams based on character counts
        anagrams = defaultdict(list)

        for s in strs:
            # Create a fixed-size list for counts of each letter (assuming 'a'-'z')
            count = [0] * 26
            for char in s:
                # Increase count for the corresponding letter
                count[ord(char) - ord('a')] += 1

            # Convert the list to a tuple, which can be used as a key in the dictionary
            anagrams[tuple(count)].append(s)

        # Return the grouped anagrams as a list of lists
        return list(anagrams.values())
