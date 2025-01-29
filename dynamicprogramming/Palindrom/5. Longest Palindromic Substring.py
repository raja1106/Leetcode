class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)                 # O(1) for assigning length of s to n.
        if n == 0:                 # O(1) for the condition check.
            return ""              # O(1) for returning an empty string.

        def expand_around_center(left, right):
            # The loop can run at most `n` times for each call, as the characters are expanded around the center.
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1           # O(1) for each decrement.
                right += 1          # O(1) for each increment.
            return s[left + 1:right] # O(1) for slicing the string (since slicing a string takes O(k), but in this case the size k is determined by the palindrome length).

        max_string = ""            # O(1) for assignment.

        for i in range(n):         # O(n) because the loop runs `n` times.
            # Odd length palindromes (single character center)
            odd_palindrome = expand_around_center(i, i)
                                    # O(n) for each call of expand_around_center. The function expands and checks up to `n` characters around the center.
            if len(odd_palindrome) > len(max_string):
                                    # O(1) because both len operations and comparison take constant time.
                max_string = odd_palindrome
                                    # O(1) for assignment.

            # Even length palindromes (two character center)
            even_palindrome = expand_around_center(i, i + 1)
                                    # O(n) for each call of expand_around_center (same as the odd case).
            if len(even_palindrome) > len(max_string):
                                    # O(1) for length comparison.
                max_string = even_palindrome
                                    # O(1) for assignment.

        return max_string          # O(1) for returning the result.


class Solution_Using_Memo: #O(n^3)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # Memoization table
        memo = {}

        # Function to check if a substring s[left:right] is a palindrome
        def is_palindrome(left, right):
            # Check if result is already in memo
            if (left, right) in memo:
                return memo[(left, right)]

            # Base case for single character or two adjacent equal characters
            if left == right:
                memo[(left, right)] = True
                return True
            elif left + 1 == right and s[left] == s[right]:
                memo[(left, right)] = True
                return True

            # Check the middle part only if s[left] == s[right]
            if s[left] == s[right]:
                if is_palindrome(left + 1, right - 1):
                    memo[(left, right)] = True
                    return True

            memo[(left, right)] = False
            return False

        max_len = 1  # At least one character is a palindrome
        longest_palindrome = s[0]  # A single character palindrome

        # Iterate over all possible substrings
        for start in range(n):
            for end in range(start + 1, n):
                if is_palindrome(start, end):
                    current_length = end - start + 1
                    if current_length > max_len:
                        max_len = current_length
                        longest_palindrome = s[start:end + 1]

        return longest_palindrome

class Solution_Using_Memo: #O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # Memoization table
        memo = {}

        # Function to check if a substring s[left:right] is a palindrome
        def is_palindrome(left, right):
            # Check if result is already in memo
            if (left, right) in memo:
                return memo[(left, right)]

            # Base case for single character or two adjacent equal characters
            if left == right:
                memo[(left, right)] = True
                return True
            elif left + 1 == right and s[left] == s[right]:
                memo[(left, right)] = True
                return True

            # Check the middle part only if s[left] == s[right]
            if s[left] == s[right]:
                if is_palindrome(left + 1, right - 1):
                    memo[(left, right)] = True
                    return True

            memo[(left, right)] = False
            return False

        max_len = 1  # At least one character is a palindrome
        longest_start = 0  # Store the start index of the longest palindrome

        # Iterate over all possible substrings
        for start in range(n):
            for end in range(start + 1, n):
                if is_palindrome(start, end):
                    current_length = end - start + 1
                    if current_length > max_len:
                        max_len = current_length
                        longest_start = start

        # Only create the substring once, at the end
        return s[longest_start:longest_start + max_len]



class Solution_Using_Bottom_Up_Approach:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        # DP table to store whether the substring s[i:j] is a palindrome
        dp = [[False] * n for _ in range(n)]
        longest_palindrome_start = 0
        max_length = 1  # A single character is always a palindrome

        # Single character substrings are palindromes
        for i in range(n):
            dp[i][i] = True

        # Fill the DP table
        for startIndex in range(n - 1, -1, -1):
            for endIndex in range(startIndex + 1, n):
                if s[startIndex] == s[endIndex]:
                    # Check if it's a two-character substring or if the substring between them is a palindrome
                    if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                        dp[startIndex][endIndex] = True

                        # Update longest palindrome if the new palindrome is longer
                        current_length = endIndex - startIndex + 1
                        if current_length > max_length:
                            longest_palindrome_start = startIndex
                            max_length = current_length

        # Return the longest palindromic substring
        return s[longest_palindrome_start:longest_palindrome_start + max_length]


s1 = "bbbab"
print(Solution().longestPalindrome(s1))  # Output: 4

s2 = "cbbd"
print(Solution().longestPalindrome(s2))  # Output: 2