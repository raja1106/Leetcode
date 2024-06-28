class Solution:
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


