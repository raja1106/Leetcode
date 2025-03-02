from collections import Counter


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        char_count = Counter()
        left = 0
        max_length = -1
        for i in range(len(s)):
            if s[i] in char_count:
                char_count[s[i]] += 1
            else:
                char_count[s[i]] = 1

            while left <= i and len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            max_length = max(max_length, i - left + 1)

        return max_length


class Solution_Bruteforce:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest_length = 0

        if k == 0:
            return 0

        if len(s) == 1 and k > 0:
            return 1

        for i in range(len(s)):
            char_set = set([s[i]])
            is_break = False
            for j in range(i + 1, len(s)):
                if s[j] not in char_set:
                    if len(char_set) == k:
                        longest_length = max(longest_length, (j - 1) - i + 1)
                        is_break = True
                        break
                    else:
                        char_set.add(s[j])
                else:
                    longest_length = max(longest_length, (j) - i + 1)
            if not is_break:
                longest_length = max(longest_length, len(s) - i)

        return longest_length