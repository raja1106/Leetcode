from typing import List, Tuple


class Solution_Bruteforce:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)

        # Try all prefixes from longest to shortest
        for i in range(n, -1, -1):
            prefix = s[:i]
            if prefix == prefix[::-1]:  # palindrome check
                suffix = s[i:]
                return suffix[::-1] + s

        return s



class Solution_Uing_KMP:#Not able to understand
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev = s[::-1]
        t = s + "#" + rev

        # Build LPS (Longest Prefix Suffix) array for KMP
        lps = [0] * len(t)
        j = 0  # length of the current matched prefix

        for i in range(1, len(t)):
            while j > 0 and t[i] != t[j]:
                j = lps[j - 1]
            if t[i] == t[j]:
                j += 1
                lps[i] = j

        L = lps[-1]              # length of longest palindromic prefix of s
        add = rev[:len(s) - L]   # reverse of the suffix that is not in pal prefix
        return add + s