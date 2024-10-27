"""
Given two strings 's1' and 's2', find the length of the longest substring which is common in both the strings.
Example 1:
Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
Example 2:
Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".
Constraints:
1 <= s1.length, s2.length <= 1000`
s1 and s2 consist of only lowercase English characters.
"""
class Solution_Bottomup:
    """
    The total time complexity is dominated by the nested loops, which iterate O(n1 * n2) times.
    Thus, the overall time complexity is O(n1 * n2).
    """
    def findLCSLength(self, s1, s2):
        n1, n2 = len(s1), len(s2)

        # Initialize a DP table with dimensions (n1+1) x (n2+1)
        dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        maxLength = 0  # Variable to store the maximum length of the common substring

        # Iterate over each character of both strings
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # If characters match, update the dp table
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    maxLength = max(maxLength, dp[i][j])  # Track the maximum length of LCS
        return maxLength  # Return the maximum length of the common substring


class Solution_Top_Down:
    def __init__(self):
        self.memo = {}

    def findLCSLength(self, s1, s2):
        return self.findLCSLengthRecursive(s1, s2, 0, 0, 0)

    def findLCSLengthRecursive(self, s1, s2, i1, i2, count):
        if i1 == len(s1) or i2 == len(s2):
            return count

        # Memoization key should include count
        if (i1, i2, count) in self.memo:
            return self.memo[(i1, i2, count)]

        c1 = count

        if s1[i1] == s2[i2]:
            c1 = self.findLCSLengthRecursive(s1, s2, i1 + 1, i2 + 1, count + 1)

        # Call the recursive function without incrementing the count to explore other paths
        c2 = self.findLCSLengthRecursive(s1, s2, i1, i2 + 1, 0) #count is reset to zero in substring problem
        c3 = self.findLCSLengthRecursive(s1, s2, i1 + 1, i2, 0)

        # Memoize the maximum value
        self.memo[(i1, i2, count)] = max(c1, c2, c3)
        return self.memo[(i1, i2, count)]

class Solution_Bruteforce:
    """
    the overall time complexity is O(n1^2 * n2), where n1 is the length of s1 and n2 is the length of s2.
    """
    def findLCSLength(self, s1, s2):
        maxLength = 0
        # Iterate over all possible substrings of s1
        for i in range(len(s1)):
            for j in range(i + 1, len(s1) + 1):
                # Extract substring of s1 from index i to j
                substring = s1[i:j]
                # Check if the current substring exists in s2
                if substring in s2:
                    # Update maxLength if a longer common substring is found
                    maxLength = max(maxLength, len(substring))
        return maxLength

class Solution_Bruteforce_better_way:
    """
    Time Complexity Analysis:
    Precomputing Substrings of s2: Generating all substrings of s2 takes O(n2^2) time, where n2 is the length of s2.
    Iterating Over Substrings of s1: Generating all substrings of s1 still takes O(n1^2) time, where n1 is the length of s1.
    Checking in the Map: Each lookup in the map is O(1) on average, making the overall complexity for this step O(n1^2).
    Therefore, the overall time complexity is O(n1^2 + n2^2).
    """
    def findLCSLength(self, s1, s2):
        # Step 1: Create a map to store all substrings of s2
        substring_map = {}
        for i in range(len(s2)):
            for j in range(i + 1, len(s2) + 1):
                substring = s2[i:j]
                substring_map[substring] = True  # Mark the substring as existing

        maxLength = 0
        # Step 2: Iterate over all possible substrings of s1 and check in the map
        for i in range(len(s1)):
            for j in range(i + 1, len(s1) + 1):
                # Extract substring of s1 from index i to j
                substring = s1[i:j]
                # Check if the current substring exists in the map
                if substring in substring_map:
                    # Update maxLength if a longer common substring is found
                    maxLength = max(maxLength, len(substring))
        return maxLength


def main():
    sol = Solution()
    print(sol.findLCSLength("abdca", "cbda"))  # Expected output: 2 ("bd")
    print(sol.findLCSLength("passport", "ppsspt"))  # Expected output: 3 ("ssp")


main()


def main():
    sol = Solution()
    print(sol.findLCSLength("abdca", "cbda"))  # Expected output: 2 ("bd")
    print(sol.findLCSLength("passport", "ppsspt"))  # Expected output: 3 ("ssp")

main()

