'''
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.



Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

'''


class Solution_Best_One:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        required_matches = len(t_counter)
        formed_matches = 0
        window_counter = Counter()
        left = 0
        min_length = float('inf')
        min_window = ""

        for i in range(len(s)):
            char = s[i]
            window_counter[char] += 1
            if char in t_counter and window_counter[char] == t_counter[char]:
                formed_matches += 1

            while left <= i and formed_matches == required_matches:
                if i - left + 1 < min_length:
                    min_length = i - left + 1
                    min_window = s[left:i + 1]
                # Contract the window from the left.
                left_char = s[left]
                window_counter[left_char] -= 1
                if left_char in t_counter and window_counter[left_char] < t_counter[left_char]:
                    formed_matches -= 1
                left += 1
            i += 1

        return min_window


class Solution_Feb_2024:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        window_counter = Counter()
        left = 0
        min_length = len(s) + 1
        min_window = ""

        def is_valid_window():
            for char, required_count in t_counter.items():
                if window_counter[char] < required_count:
                    return False
            return True

        for right in range(len(s)):
            window_counter[s[right]] += 1

            while left <= right and is_valid_window():
                # Update the minimum window if the current one is smaller.
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right + 1]
                # Shrink the window from the left regardless of whether we updated the minimum.
                window_counter[s[left]] -= 1
                if window_counter[s[left]] == 0:
                    del window_counter[s[left]]
                left += 1

        return min_window


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ''
        t_map = Counter(t)
        k = len(t)
        s_map={}

        for i in range(k):
            s_map[s[i]] = s_map.get(s[i], 0)+1

        if t_map == s_map:
            return s[:k]
        min_window = len(s)
        ans=''
        left=0
        def ismatching(s_map,t_map):

            for char,count in t_map.items():
                if char not in s_map and s_map[char] < count:
                    return False

            return True

        for i in range(k,len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            while left <= i and ismatching(s_map,t_map):
                if min_window >= i-left+1:
                    ans = s[left:i + 1]
                    min_window= i-left+1
                s_map[s[left]] = s_map.get(s[left], 0)-1
                left += 1
        return ans

    def minWindow_mons(self, source: str, target: str) -> str:
        # Create a counter for the target to keep a record of each character's frequency
        target_counter = Counter(target)
        window_counter = Counter()  # This will keep a count of characters in the current window
        valid_char_count = 0  # Number of characters that meet the target criteria
        left = 0  # Left pointer to shrink the window
        min_left = -1  # Left boundary index of the minimum window
        min_size = inf  # Initialize min_size to positive infinity

        # Iterate over each character in the source string
        for i, char in enumerate(source):
            # Include current character in the window
            window_counter[char] += 1
            # If the current character is needed and the window contains enough of this character
            if target_counter[char] >= window_counter[char]:
                valid_char_count += 1

            # If the window has all the characters needed
            while valid_char_count == len(target):
                # If this window is smaller than the minimum so far, update minimum size and index
                if i - left + 1 < min_size:
                    min_size = i - left + 1
                    min_left = left

                # If the character at the left pointer is less frequent in the window than in the target,
                # reducing it further would break the window condition
                if target_counter[source[left]] >= window_counter[source[left]]:
                    valid_char_count -= 1

                # Shrink the window from the left
                window_counter[source[left]] -= 1
                left += 1

        # If no window meets the criteria, return an empty string
        return '' if min_left < 0 else source[min_left:min_left + min_size]

    def minWindow_Notworking(self, s: str, t: str) -> str:
        left=0
        smap, tmap = {},{}
        min_length=len(s)+1
        start_index,end_index =0,0
        for i in range(len(t)):
            if t[i] in tmap:
                tmap[t[i]] += 1
            else:
                tmap[t[i]] = 1

        for i in range(len(s)):
            if s[i] in smap:
                smap[s[i]] += 1
            else:
                smap[s[i]] = 1

            while left <= i and len(smap)>len(tmap):
                smap[s[left]] -= 1
                if smap[s[left]] == 0:
                    del smap[s[left]]
                left += 1

            if smap == tmap:
                if (i-left+1) <min_length:
                    start_index =left
                    end_index=i
        return s[start_index:end_index+1]
