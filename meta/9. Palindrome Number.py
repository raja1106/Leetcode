class Solution_inplace: #T(n) = O(n) S(n) = O(1)
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert the integer to a string
        s = str(x)

        # Use two-pointer technique to check for palindrome
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True

class Solution_with_not_in_place:  #T(n) = O(n) S(n) = O(n)
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        s = str(x)
        return s == s[::-1]
