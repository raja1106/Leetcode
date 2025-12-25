class Solution:
    def minSwaps(self, s: str) -> int:
        """
        ][][

        ]]]][[[[

        count 1 1

        you are receiving closed when open is 0

        open += 1

        count = 1



        [[][]]

        """
        balance = 0
        swap_needed = 0
        for ch in s:
            if ch == ']':
                if balance == 0:
                    swap_needed += 1
                    balance += 1
                else:
                    balance -= 1
            else:
                balance += 1

        return swap_needed