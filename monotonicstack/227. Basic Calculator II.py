class Solution:
    def calculate(self, s: str) -> int:
        # Stack to hold numbers and intermediate results
        stack = []

        def apply_operator(operand1, operand2, operator):
            """Apply the operator on two operands and return the result."""
            if operator == '*':
                return operand1 * operand2
            elif operator == '/':
                return int(operand1 / operand2)  # Ensure truncation towards zero for integer division

        index = 0
        current_sign = 1  # 1 for positive, -1 for negative

        while index < len(s):
            char = s[index]

            if char == '+':
                current_sign = 1
                index += 1
            elif char == '-':
                current_sign = -1
                index += 1
            elif char in ('*', '/'):
                stack.append(char)
                index += 1
            elif char.isdigit():
                number = 0
                # Parse the full number in case it's more than one digit
                while index < len(s) and s[index].isdigit():
                    number = number * 10 + int(s[index])
                    index += 1

                # Handle multiplication or division immediately
                if stack and stack[-1] in ('*', '/'):
                    operator = stack.pop()
                    operand1 = stack.pop()
                    result = apply_operator(operand1, number, operator) * current_sign
                    stack.append(result)
                else:
                    stack.append(number * current_sign)

                # Reset sign for the next number
                current_sign = 1
            else:
                # Skip whitespace or any non-relevant character
                index += 1

        # Return the sum of all numbers in the stack, which represents the final result
        return sum(stack)
