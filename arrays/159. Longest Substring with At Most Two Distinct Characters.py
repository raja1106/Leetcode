from builtins import str
from collections import Counter


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_count = Counter()
        left = 0
        max_length = -1
        for i in range(len(s)):
            char_count[s[i]] += 1
            while left <= i and len(char_count) > 2:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, i - left + 1)

        return max_length