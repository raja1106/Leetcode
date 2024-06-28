from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        char_map = Counter()
        max_count = 0  # To keep track of the count of the most frequent character in the current window

        for i in range(len(s)):
            char_map[s[i]] += 1
            max_count = max(max_count, char_map[s[i]])
            temp = i - left + 1
            # If the number of characters to replace exceeds k, shrink the window
            while left <= i and (i - left + 1) - max_count > k:
                char_map[s[left]] -= 1
                left += 1

            max_length = max(max_length, i - left + 1)

        return max_length


obj = Solution()
ans = obj.characterReplacement("ABAB", 1)
print(ans)
