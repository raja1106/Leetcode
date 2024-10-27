from typing import List


class Solution:
   """
   T(n) = O(S), where S is the total number of characters across all strings. This solution is more efficient when all strings are nearly the same length and the common prefix is long.
   """
   def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)

        common_prefix = []

        for k in range(min_length):
            current_letter = strs[0][k]
            if all(s[k] == current_letter for s in strs):
                common_prefix.append(current_letter)
            else:
                break

        return ''.join(common_prefix)


from typing import List


class Solution_More_Efficient:
    """
In the worst case, the time complexity can be approximated as O(n×L), where

n is the number of strings, and L is the length of the first string.

This is because for each character position, we perform up to n comparisons, iterating over all strings.
when  the common prefix is short, the given code can terminate early,
making it more efficient. However, if there is a long common prefix that spans most of the strings' lengths,
the time complexity approaches 𝑂(𝑆). O(S), similar to the previous solution.

    """
    def longestCommonPrefix(self, strings: List[str]) -> str:
        # Check for an empty input list
        if not strings:
            return ""

        # Early return if the first string is empty
        first_string = strings[0]
        if not first_string:
            return ""

        # Iterate over each character position in the first string
        for index in range(len(first_string)):
            current_char = first_string[index]
            # Check if the current character matches in all other strings
            for string in strings[1:]:
                # If we reach the end of a string or find a mismatch, return the current prefix
                if index >= len(string) or string[index] != current_char:
                    return first_string[:index]

        # If the loop completes, the entire first string is the common prefix
        return first_string

