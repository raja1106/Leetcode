from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map1 = Counter()
        map2 = Counter()
        anagram_indices=[]
        k = len(p)
        if len(s) < k:
            return anagram_indices
        for i in range(k):
            if p[i] in map1:
                map1[p[i]] += 1
            else:
                map1[p[i]] = 1

        for j in range(k):
            if s[j] in map2:
                map2[s[j]] += 1
            else:
                map2[s[j]] = 1

        if (map1 == map2):
            anagram_indices.append(0)

        for j in range(k, len(s)):
            if s[j] in map2:
                map2[s[j]] += 1
            else:
                map2[s[j]] = 1

            map2[s[j - k]] -= 1
            if map2[s[j - k]] == 0:
                map2.pop(s[j - k])
            if (map1 == map2):
                anagram_indices.append(j-k+1)
        return anagram_indices
