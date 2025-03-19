class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        result = []
        index1 = len(num1) - 1
        index2 = len(num2) - 1

        while index1 >= 0 or index2 >= 0 or carry:
            digit1 = int(num1[index1]) if index1 >= 0 else 0
            digit2 = int(num2[index2]) if index2 >= 0 else 0

            total = digit1 + digit2 + carry
            carry, digit = divmod(total, 10)

            result.append(str(digit))
            index1 -= 1
            index2 -= 1

        result.reverse()
        return ''.join(result)


class Solution2:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Adds two non-negative integers represented as strings and returns the sum as a string.

        Example:
            Input: num1 = "11", num2 = "123"
            Output: "134"
        """
        index1 = len(num1) - 1
        index2 = len(num2) - 1
        carry = 0
        result_digits = []

        while index1 >= 0 or index2 >= 0 or carry:
            # Get the current digit from num1 if available, else use 0
            if index1 >= 0:
                digit1 = int(num1[index1])
                index1 -= 1
            else:
                digit1 = 0

            # Get the current digit from num2 if available, else use 0
            if index2 >= 0:
                digit2 = int(num2[index2])
                index2 -= 1
            else:
                digit2 = 0

            # Compute the sum of digits and the carry
            digit_sum = digit1 + digit2 + carry
            current_digit = digit_sum % 10
            carry = digit_sum // 10

            # Append the current digit (as a string) to the result list
            result_digits.append(str(current_digit))

        # Reverse the result to obtain the correct order and join into a single string
        return ''.join(reversed(result_digits))
