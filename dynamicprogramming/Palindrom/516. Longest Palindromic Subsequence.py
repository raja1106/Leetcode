class Solution_BruteForce:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        def lps_helper(s,start,end):
            if start > end:
                return 0
            if start == end:
                return 1
            if s[start] == s[end]:
                return 2+lps_helper(s,start+1,end-1)
            else:
                case1 = lps_helper(s,start+1,end)
                case2 = lps_helper(s,start,end-1)
                return max(case1,case2)

        return lps_helper(s,0,n-1)


class Solution_Topdown:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        memo = {}

        def lps_helper(s, start, end):
            memo_key = (start, end)
            if memo_key in memo:
                return memo[memo_key]

            if start > end:
                return 0
            elif start == end:
                memo[memo_key] = 1
            elif s[start] == s[end]:
                memo[memo_key] = 2 + lps_helper(s, start + 1, end - 1)
            else:
                case1 = lps_helper(s, start + 1, end)
                case2 = lps_helper(s, start, end - 1)
                memo[memo_key] = max(case1, case2)
            return memo[memo_key]

        return lps_helper(s, 0, n - 1)

class Solution_Bottom_Up:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # dp[i][j] stores the length of LPS from index 'i' to index 'j'
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # every sequence with one element is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1

        for startIndex in range(n - 1, -1, -1):
            for endIndex in range(startIndex + 1, n):
            # case 1: elements at the beginning and the end are the same
                if s[startIndex] == s[endIndex]:
                    dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
                else:  # case 2: skip one element either from the beginning or the end
                    dp[startIndex][endIndex] = max(dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])
        return dp[0][n - 1]
