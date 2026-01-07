from functools import lru_cache
from typing import List, Tuple

class Solution_top_down:
    def numDecodings(self, s: str) -> int:
        """
        Top-down DP (memoization):
        dp(i) = number of ways to decode substring s[i:].

        Transitions:
        - If s[i] == '0' => 0 ways (no letter maps to 0)
        - Take 1 digit: s[i] in '1'..'9' => dp(i+1)
        - Take 2 digits: 10..26 => dp(i+2)

        Time:  O(n)
        Space: O(n) for memo + recursion stack
        """
        n = len(s)
        if n == 0:
            return 0

        @lru_cache(maxsize=None)
        def dp(i: int) -> int:
            # Reached end successfully
            if i == n:
                return 1

            # Leading zero can't be decoded
            if s[i] == '0':
                return 0

            # Take one digit
            ways = dp(i + 1)

            # Take two digits if valid (10..26)
            if i + 1 < n:
                two = int(s[i:i+2])
                if 10 <= two <= 26:
                    ways += dp(i + 2)

            return ways

        return dp(0)

# ----------------------------
# Tests (as you requested)
# ----------------------------
def _run_tests():
    sol = Solution_top_down()
    tests: List[Tuple[str, int]] = [
        ("12", 2),       # "AB", "L"
        ("226", 3),      # "BZ", "VF", "BBF"
        ("06", 0),       # invalid
        ("0", 0),
        ("10", 1),       # "J"
        ("101", 1),      # "JA"
        ("27", 1),       # "BG" (27 not valid as two-digit)
        ("11106", 2),    # "AAJF", "KJF"
        ("", 0),
        ("1", 1),
        ("2101", 1),     # "U A"?? actually "21 01" invalid, "2 10 1" => 1
    ]

    for s, expected in tests:
        got = sol.numDecodings(s)
        assert got == expected, f"FAIL s={s}: got {got}, expected {expected}"
    print("All tests passed.")

_run_tests()


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # Edge case: If string starts with '0', it's not decodable
        if s[0] == '0':
            return 0

        # DP array to store the number of ways to decode up to index i
        dp = [0] * n
        dp[0] = 1  # Only one way to decode a single character (if it's not '0')

        # Base case for two-character strings
        if n == 1:
            return dp[0]

        # Handle the second character
        if s[1] == '0':  # Only valid if it's "10" or "20"
            if s[0] in {'1', '2'}:
                dp[1] = 1
            else:
                return 0  # Invalid encoding (e.g., "30" is invalid)
        elif 10 <= int(s[:2]) <= 26:
            dp[1] = 2  # Two ways: decode separately or as a pair
        else:
            dp[1] = 1  # Decode separately only

        # Iterate through the string and build the DP array
        for i in range(2, n):
            if s[i] != '0':  # Single-digit decode possible
                dp[i] = dp[i - 1]
            if s[i - 1] in {'1', '2'} and 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2]  # Two-digit decode possible

        return dp[-1]
