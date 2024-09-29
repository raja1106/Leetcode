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

