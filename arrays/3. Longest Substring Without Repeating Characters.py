
def lengthOfLongestSubstring(self, s: str) -> int: #Efficient Approach O(n)
    char_index = {}
    max_length = 0
    left = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    return max_length


class Solution: #O(2n) --> O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_length = 0
        window_counter=Counter()
        for i in range(len(s)):
            window_counter[s[i]] += 1

            while left <= i and window_counter[s[i]] > 1:
                window_counter[s[left]] -= 1
                left += 1
            max_length = max(max_length,i-left+1)

        return max_length

    def lengthOfLongestSubstringUsingSet(self, s: str) -> int:
        left = 0
        max_length = 0
        window_set = set()
        for i in range(len(s)):

            while left <= i and s[i] in window_set:
                window_set.remove(s[left])
                left += 1
            window_set.add(s[i])
            max_length = max(max_length, i - left + 1)

        return max_length


