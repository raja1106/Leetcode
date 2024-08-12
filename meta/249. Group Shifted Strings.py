from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def getKey(s: str) -> tuple:
            # Calculate the "shift key" for the string
            key = []
            for i in range(1, len(s)):
                # The difference between each character in the string, wrapped by 26 (number of letters in the alphabet)
                diff = (ord(s[i]) - ord(s[i - 1])) % 26
                key.append(diff)
            # Convert the list of differences to a tuple to be used as a hashable key
            return tuple(key)

        # Dictionary to hold groups of strings with the same shift key
        groups = defaultdict(list)

        # Iterate over each string
        for s in strings:
            # Get the shift key for the string
            key = getKey(s)
            # Add the string to the group corresponding to the shift key
            groups[key].append(s)

        # Return the grouped strings as a list of lists
        return list(groups.values())


sol = Solution()
print(sol.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
