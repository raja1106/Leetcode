from collections import Counter
from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_length, p_length = len(s), len(p)
        result = []
        if s_length < p_length:
            return result

        pattern_count = Counter(p)
        window_count = Counter(s[:len(p)])

        if pattern_count == window_count:
            result.append(0)
        k = len(p)
        for i in range(p_length, s_length):
            window_count[s[i]] += 1
            window_count[s[i-k]] -= 1
            if window_count[s[i-k]] == 0:
                del window_count[s[i-k]]

            if pattern_count == window_count:
                result.append(i-k+1)
        return result

    def findAnagramsOldApproach(self, s: str, p: str) -> List[int]:
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
