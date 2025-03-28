class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_index = 0
        matched_count = 0

        for s_char in s:
            found_match = False
            while t_index < len(t):
                t_char = t[t_index]
                if s_char == t_char:
                    found_match = True
                    t_index += 1
                    matched_count += 1
                    break
                t_index += 1

            if not found_match:
                return False

        return matched_count == len(s)

class Solution_Another_Way:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_s, idx_t = 0, 0
        while idx_s < len(s) and idx_t < len(t):
            if s[idx_s] == t[idx_t]:
                idx_s += 1
            idx_t += 1
        return idx_s == len(s)


from collections import defaultdict
import bisect


class DictionarySubsequenceChecker:
    def __init__(self, t: str):
        """
        Preprocess the string t by building a dictionary (char_positions).
        For each character c in t, store a sorted list of all indices where c appears.
        """
        self.char_positions = defaultdict(list)
        for index, char in enumerate(t):
            self.char_positions[char].append(index)

    def is_subsequence(self, s: str) -> bool:
        """
        Check if s is a subsequence of the preprocessed string t.
        Uses binary search (bisect) to find the next valid position for each character in s.
        """
        current_pos = -1  # Tracks the position in t we have matched so far

        for char in s:
            # If char does not exist in t at all, s cannot be a subsequence
            if char not in self.char_positions:
                return False

            # Retrieve the list of positions for this character
            positions = self.char_positions[char]

            # Use binary search to find the smallest index in positions that is > current_pos
            # We look for the leftmost position >= (current_pos + 1)
            next_index = bisect.bisect_left(positions, current_pos + 1)

            # If next_index is out of range, it means there is no position for this char
            # after current_pos
            if next_index == len(positions):
                return False

            # Update current_pos to the position where we matched this char
            current_pos = positions[next_index]

        return True


# --------------------------
# Example Usage:
# --------------------------

# Suppose t is very large, and we have multiple queries s1, s2, s3...
t = "abcdeabcfg"

checker = DictionarySubsequenceChecker(t)

print(checker.is_subsequence("ace"))  # True  (positions: a->0, c->2, e->4)
print(checker.is_subsequence("abcf"))  # True  (positions: a->0, b->1, c->2, f->8)
print(checker.is_subsequence("aecc"))  # False (the second 'c' is found before the 'e' or out of order)
print(checker.is_subsequence("abzz"))  # False ('z' does not exist in t)
