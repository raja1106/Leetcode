class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        ans = 0
        for c in s:
            if c == '(':
                balance += 1
            else:
                balance -= 1
            # If balance is negative, we have an unmatched ')'
            if balance < 0:
                ans += 1
                balance = 0  # reset balance to 0 after accounting for an unmatched ')'
        # Add any unmatched '('
        ans += balance
        return ans
