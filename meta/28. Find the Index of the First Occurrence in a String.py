class Solution_Efficient_Space_complexity: #S(n):O(1)
    def strStr(self, haystack: str, needle: str) -> int:
        # Length of the haystack and needle strings
        haystack_length, needle_length = len(haystack), len(needle)

        # Check all possible starting positions of needle in haystack
        for start in range(haystack_length - needle_length + 1):
            # If the substring matching the needle's length equals the needle, return the start index
            if haystack[start: start + needle_length] == needle:
                return start

        # If the needle is not found in haystack, return -1
        return -1
class Solution_Sliding_Window_Template:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is an empty string, return 0 as per convention.
        if not needle:
            return 0

        m = len(needle)
        n = len(haystack)

        # If needle is longer than haystack, it can't be a substring.
        if m > n:
            return -1

        # Initialize the sliding window with the first m characters of haystack.
        window = haystack[:m]
        if window == needle:
            return 0

        # Slide the window from index m to the end of haystack.
        for i in range(m, n):
            # "Slide" the window:
            # Remove the first character of the current window (window[1:])
            # and add the new character haystack[i] at the end.
            window = window[1:] + haystack[i]
            # The starting index of the current window is (i - m + 1)
            if window == needle:
                return i - m + 1

        # If no matching window was found, return -1.
        return -1


class Solution_April_2024:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)
        i = 0
        while i < haystack_length:  # O(m)
            if haystack[i] == needle[0]:
                sub_string = haystack[i:i + needle_length]  # O(n)
                if sub_string == needle:
                    return i
            i += 1

        return -1

