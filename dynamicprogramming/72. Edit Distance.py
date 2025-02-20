class Solution_Using_Bruteforce:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        This function computes the minimum number of operations (insertions, deletions, and replacements)
        required to convert word1 into word2 using a recursive DFS approach.

        Example:
        word1 = "horse", word2 = "ros"
        Output: 3
        Explanation:
        - horse -> rorse (replace 'h' with 'r')
        - rorse -> rose (delete 'r')
        - rose -> ros (delete 'e')
        """

        m, n = len(word1), len(word2)
        min_val = float('inf')  # Initialize minimum edit distance as infinity

        def dfs(i, j, current_operations):
            """
            Recursive DFS function to compute edit distance.

            Args:
            - i: Current index in word1
            - j: Current index in word2
            - current_operations: Number of operations performed so far

            Base case:
            - If one of the strings is fully traversed, add remaining operations.
            - If i == m (end of word1), insert the remaining characters from word2.
            - If j == n (end of word2), delete the remaining characters from word1.

            Recursive steps:
            - If characters match, move to the next character in both strings.
            - Otherwise, try all three operations:
                1. Insert a character (move j forward in word2)
                2. Delete a character (move i forward in word1)
                3. Replace a character (move both i and j forward)
            """
            nonlocal min_val  # Allows updating min_val from within the nested function

            # Base Case: If one of the strings is exhausted, calculate remaining operations
            if i == m or j == n:
                current_operations += (m - i) + (n - j)  # Insert remaining from word2 or delete remaining from word1
                min_val = min(min_val, current_operations)  # Update the minimum edit distance found
                return

            if word1[i] == word2[j]:  # Characters match, move both pointers without additional cost
                dfs(i + 1, j + 1, current_operations)
            else:
                # Try all three possible operations:
                dfs(i, j + 1, current_operations + 1)  # Insert a character (move j forward)
                dfs(i + 1, j, current_operations + 1)  # Delete a character (move i forward)
                dfs(i + 1, j + 1, current_operations + 1)  # Replace a character (move both forward)

        # Start the DFS traversal from index 0 of both words with 0 operations
        dfs(0, 0, 0)

        return min_val  # Return the minimum edit distance found

class Solution_Using_BottomUP:
    def minDistance(self, word1: str, word2: str) -> int:
        # If both strings are empty, the edit distance is 0
        if not word1 and not word2:
            return 0

        m, n = len(word1), len(word2)

        # Create a DP table initialized with "infinity" (though unnecessary)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Case 1: If word1 is empty, convert empty string to word2 (insert all characters)
        for row in range(m + 1):
            dp[row][0] = row  # It takes 'row' deletions to convert word1[0:row] to an empty string

        # Base Case 2: If word2 is empty, convert word1 to empty string (delete all characters)
        for col in range(n + 1):
            dp[0][col] = col  # It takes 'col' insertions to convert an empty string to word2[0:col]

        # Fill the DP table bottom-up
        for i in range(1, m + 1):  # Iterate through word1
            for j in range(1, n + 1):  # Iterate through word2
                if word1[i - 1] == word2[j - 1]:  # If characters match, no operation needed
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Compute the minimum operation required:
                    # 1. Delete a character from word1: dp[i-1][j] + 1
                    # 2. Insert a character into word1: dp[i][j-1] + 1
                    # 3. Replace a character in word1: dp[i-1][j-1] + 1
                    dp[i][j] = min(dp[i - 1][j] + 1,  # Deletion
                                   dp[i][j - 1] + 1,  # Insertion
                                   dp[i - 1][j - 1] + 1)  # Replacement

        # The final answer is stored in dp[m][n], which represents transforming word1[:m] to word2[:n]
        return dp[m][n]


class Solution_Another_Bottom_Up_Approach:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create DP table
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Cases:
        # If word1 is exhausted, insert all remaining characters from word2
        for j in range(n + 1):
            dp[m][j] = n - j  # Remaining insertions required

        # If word2 is exhausted, delete all remaining characters from word1
        for i in range(m + 1):
            dp[i][n] = m - i  # Remaining deletions required

        # Fill the DP table bottom-up (reverse order)
        for i in range(m - 1, -1, -1):  # Start from last row
            for j in range(n - 1, -1, -1):  # Start from last column
                if word1[i] == word2[j]:  # Characters match, move diagonally
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j],  # Delete
                        dp[i][j + 1],  # Insert
                        dp[i + 1][j + 1]  # Replace
                    )

        return dp[0][0]  # The answer is now at the top-left cell

