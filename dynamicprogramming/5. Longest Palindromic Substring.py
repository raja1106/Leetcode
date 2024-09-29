class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # Memoization table
        memo = {}

        # Function to check if a substring is a palindrome
        def is_palindrome(left, right):
            # Check if result is already in memo
            if (left, right) in memo:

                return memo[(left, right)]

            while left < right:
                if s[left] != s[right]:
                    memo[(left, right)] = False  # Memoize the result
                    return False
                left += 1
                right -= 1

            memo[(left, right)] = True  # Memoize the result
            return True

        max_val = 1
        max_string = s[0]

        # Loop over all possible substrings
        for start in range(n):
            for end in range(start + 1, n):
                if is_palindrome(start, end):
                    if (end + 1) - start > max_val:
                        max_val = end - start
                        max_string = s[start:end + 1]

        return max_string

s1 = "bbbab"
print(Solution().longestPalindrome(s1))  # Output: 4

s2 = "cbbd"
print(Solution().longestPalindrome(s2))  # Output: 2