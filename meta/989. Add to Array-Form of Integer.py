from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        """
       num = [2,7,4], k = 181

       185

     4 5 5

        """

        carry = k
        result = []
        for digit in reversed(num):
            current_result = carry + digit
            carry, current_digit = divmod(current_result, 10)
            result.append(current_digit)

        if carry:
            result.extend([int(digit_str) for digit_str in reversed(str(carry))])

        return result[::-1]
