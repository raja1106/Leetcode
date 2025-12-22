class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            # Remove digits from the stack if they are bigger than the current digit
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If we still have digits to remove, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"


class Solution_Bruteforce:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        Input: num = "1432219", k = 3
        1432219
        1 4 3 2 2 1 9

        12345

        1 -> 2345
        2 -> 1345
        3 -> 1245
        4 -> 1235
        5 -> 1234

        5632

        5 -> 632
        6 -> 532
        3 -> 562
        2-> 563

        5632

        56 -> 32
        53 -> 62
        52 -> 63
        63-> 52
        32 -> 56



        """
        min_value = int(num)

        def helper(i, remaining, current_val_str):
            nonlocal min_value
            if i == len(num):
                current_val = int(current_val_str) if current_val_str else 0
                if remaining == 0 and current_val < min_value:
                    min_value = current_val
                return

            # exclude
            if remaining > 0:
                helper(i + 1, remaining - 1, current_val_str)
            # include
            helper(i + 1, remaining, current_val_str + num[i])
            return

        helper(0, k, '')
        return str(min_value)





















