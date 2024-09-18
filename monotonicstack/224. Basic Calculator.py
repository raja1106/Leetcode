class Solution:
    def calculate(self, expression: str) -> int:
        def parse_number(expression, index):
            """Parses multi-digit numbers and returns the number and updated i."""
            num = 0
            while index < len(expression) and expression[index].isdigit():
                num = num * 10 + int(expression[index])
                index += 1
            return num, index
        stack = []
        current_operator = '+'
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isdigit():
                number, i = parse_number(expression, i)
                if current_operator == '+':
                    stack.append(number)
                elif current_operator == '-':
                    stack.append(-number)
                continue  # Skip the increment below since i is already updated

            elif char == '+':
                current_operator = '+'

            elif char == '-':
                current_operator = '-'

            elif char == '(':
                stack.append(current_operator)
                stack.append('(')
                current_operator = '+'  # Reset operator for the new expression block

            elif char == ')':
                temp_sum = 0
                while stack and stack[-1] != '(':
                    temp_sum += stack.pop()
                stack.pop()  # Remove the opening '('

                # Apply the operator before the parenthesis block
                if stack and stack[-1] in ('+', '-'):
                    operator_before_parenthesis = stack.pop()
                    if operator_before_parenthesis == '+':
                        stack.append(temp_sum)
                    elif operator_before_parenthesis == '-':
                        stack.append(-temp_sum)
            i += 1

        return sum(stack)
