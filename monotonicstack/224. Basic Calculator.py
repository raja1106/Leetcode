class Solution:
    def calculate(self, s: str) -> int:
        st = []
        sign_operator = 1

        def parse_number(k):
            j = k
            while j< len(s) and s[j].isdigit(): #(111) k=1, j=4
                j += 1
            return (j-1,s[k:j])

        i = 0
        while i < len(s):
            ch = s[i]
            if ch == '(':
                if sign_operator == -1:
                    st.append('-')
                sign_operator = 1
                st.append(ch)
            elif ch == '+':
                sign_operator = 1
            elif ch == '-':
                sign_operator = -1
            elif ch.isdigit():
                new_index,new_number_str = parse_number(i)
                new_number = int(new_number_str)
                i = new_index
                st.append(new_number*sign_operator)
            elif ch == ')':
                local_calculation = 0
                while st and st[-1] != '(':
                    local_calculation += st.pop()
                st.pop() #to pop '('
                if st and st[-1] == '-':
                    st.pop()
                    st.append(local_calculation*-1)
                else:
                    st.append(local_calculation)
            i += 1

        return sum(st)

class Solution_Old_approach:
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
