class Solution:
    """
            Input: s = "aab"
            Output: [["a","a","b"],["aa","b"]]

                        -  i = 0
                    a.     aa.       aab

                a ab.     b.            ''

            b.    ""

    """
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(i, j):

            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def helper(i, slate):
            """
            Backtracking function that builds all palindromic partitions.
            :param i: The current starting index in the string 's'.
            :param slate: A list of palindromic substrings found so far.
            """
            # If 'i' has reached the end of the string, we've found a valid partition.
            # Append a copy of 'slate' to 'result' and return.
            if i == len(s):
                result.append(list(slate))
                return

            # Try to partition the string at each possible 'j' from 'i' to len(s) - 1
            for j in range(i, len(s)):
                # If the substring s[i:j+1] is a palindrome,
                # add it to 'slate' and recurse for the next part of the string.
                if is_palindrome(i, j):
                    slate.append(s[i:j + 1])
                    helper(j + 1, slate)
                    # Backtrack: remove the last palindrome to explore new partitions
                    slate.pop()

        # Initiate the recursive backtracking from index 0 with an empty 'slate'
        helper(0, [])
        return result
