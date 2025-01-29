class Solution_Using_expandAroundCenter:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                # s[left:right+1] is a palindrome
                count += 1
                left -= 1
                right += 1
            return count

        total_palindromes = 0
        for i in range(len(s)):
            # Odd-length palindromes
            total_palindromes += expandAroundCenter(i, i)
            # Even-length palindromes
            total_palindromes += expandAroundCenter(i, i + 1)

        return total_palindromes

class Solution_Using_DP_Bottom_up:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        count = 0

        # Single character substrings are palindromes
        for i in range(n):
            dp[i][i] = True
            count += 1

        for startIndex in range(n - 1, -1, -1): # You can put range range(n - 2, -1, -1) as well
            for endIndex in range(startIndex + 1, n):
                if s[startIndex] == s[endIndex]:
                    # if it's a two character string or if the remaining string is a palindrome too
                    if endIndex - startIndex == 1 or dp[startIndex + 1][endIndex - 1]:
                        dp[startIndex][endIndex] = True
                        count += 1

        return count


class Solution_Using_Memo:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0  # Return 0 for an empty string

        memo = {}
        count = 0

        # Function to check if a substring s[start:end] is a palindrome
        def is_palindrome(start, end):
            # Check the memo table to avoid rechecking
            if (start, end) in memo:
                return memo[(start, end)]

            # Base case for single character or two adjacent equal characters
            if start == end:
                memo[(start, end)] = True
                return True
            elif start+1 == end and s[start] == s[end]:
                memo[(start, end)] = True
                return True


            # If the two ends are the same, check the middle part
            if s[start] == s[end]:
                if is_palindrome(start + 1, end - 1):
                    memo[(start, end)] = True
                    return True

            # Otherwise, it's not a palindrome
            memo[(start, end)] = False
            return False

        # Iterate over all possible substrings
        for start in range(n):
            for end in range(start, n):
                if is_palindrome(start, end):
                    count += 1

        return count
