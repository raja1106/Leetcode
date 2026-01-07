class Solution_Bruteforce:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
class Solution_Bruteforce_anotherway:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        Check if a string can be constructed by repeating a substring.

        The algorithm works by concatenating the string with itself and checking
        if the original string appears in the middle portion (excluding the first
        and last occurrence).

        If the string is made of repeated substrings, it will appear again before
        reaching the end of the doubled string.

        Args:
            s: Input string to check for repeated pattern

        Returns:
            True if the string consists of a repeated substring, False otherwise
        """
        # Concatenate the string with itself to create a doubled string
        doubled_string = s + s

        # Search for the original string starting from index 1 (skip the first character)
        # This avoids finding the string at position 0
        first_occurrence_after_start = doubled_string.index(s, 1)

        # If the string appears before reaching the end (at position len(s)),
        # it means the original string contains a repeated pattern
        return first_occurrence_after_start < len(s)