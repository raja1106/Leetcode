class Solution:
    def calculate(self, s: str) -> int:
        value, n = 0, len(s)
        sign = '+'
        stack = []
        for i, char in enumerate(s):
            if char.isdigit():
                value = value * 10 + int(char)
            # If we reach the end of the string or encounter an operator.
            if char in '+-*/' or i == n - 1:
                # Perform an action depending on the last sign observed.
                if sign == '+':
                    # If the sign is plus, push the current value onto the stack.
                    stack.append(value)
                elif sign == '-':
                    # If the sign is minus, push the negative of the value onto the stack.
                    stack.append(-value)
                elif sign == '*':
                    stack.append(stack.pop() * value)
                elif sign == '/':
                    stack.append(int(stack.pop() / value))

                # Update the sign to the current operator.
                sign = char
                # Reset 'value' for the next number.
                value = 0
        return sum(stack)
solution = Solution()

# Test cases
print(solution.calculate("3+2*2"))  # Output: 7
print(solution.calculate(" 3/2 "))  # Output: 1
print(solution.calculate(" 3+5 / 2 "))  # Output: 5
print(solution.calculate("10-3*2"))  # Output: 4
print(solution.calculate("14-3/2"))  # Output: 13
print(solution.calculate("2*3*2"))  # Output: 12
