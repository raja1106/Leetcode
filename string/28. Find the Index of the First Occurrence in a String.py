class Solution_using_sliding_window:
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

class Solution_KMP:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Build LPS array
        lps = [0] * len(needle)
        j = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j - 1]
            if needle[i] == needle[j]:
                j += 1
            lps[i] = j

        # Search
        i = j = 0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
                if j == len(needle):
                    return i - j
            else:
                if j > 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return -1
