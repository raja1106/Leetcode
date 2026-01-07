class Solution:
    def validPalindrome(self, string: str) -> bool:
        # Helper function to check if substring string[left:right+1] is a palindrome
        def is_palindrome(left, right):
            while left < right:
                if string[left] != string[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        left, right = 0, len(string) - 1  # Initialize pointers at both ends of the string

        # Iterate while the two pointers don't cross each other
        while left < right:
            # If the characters at the current pointers don't match
            if string[left] != string[right]:
                # Check for palindrome by removing one character - either from the left or right
                # If either case returns true, the function returns true
                return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
            # Move both pointers towards the center
            left, right = left + 1, right - 1

        # If the string is a palindrome or can be made into one by removing a single character
        return True


class Solution_Another_Approach:
    def validPalindrome(self, s: str) -> bool:
        """
        s = "abca"
        """
        def is_palindrome(left, right, deletions_left):
            if left >= right:
                return True

            match_case = skip_left = skip_right = False

            if s[left] == s[right]:
                match_case = is_palindrome(left + 1, right - 1, deletions_left)
            elif deletions_left > 0:
                skip_left = is_palindrome(left + 1, right, deletions_left - 1)
                skip_right = is_palindrome(left, right - 1, deletions_left - 1)

            return match_case or skip_left or skip_right

        return is_palindrome(0, len(s) - 1, 1)
print(Solution().validPalindrome('radadkar'))



