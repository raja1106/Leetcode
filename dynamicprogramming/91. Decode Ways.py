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
