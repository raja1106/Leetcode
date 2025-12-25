class Solution:
    def calculate(self, s: str) -> int:

        def parse_number(idx):
            k = idx
            while k < len(s) and s[k].isdigit():
                k += 1
            return (k - 1, s[idx:k])

        def apply_operator(operand1, operand2, operator):
            if operator == '*':
                return operand1 * operand2
            else:
                return int(operand1 / operand2)

        i = 0
        st = []
        current_sign = 1
        s = s.strip().replace(' ', '')
        while i < len(s):
            ch = s[i]

            if ch.isdigit():
                new_idx, new_number_str = parse_number(i)
                i = new_idx
                if st and st[-1] in ('*', '/'):
                    operator = st.pop()
                    operand1 = st.pop()
                    partial_result = apply_operator(operand1, int(new_number_str), operator)
                    st.append(partial_result * current_sign)
                    current_sign = 1
                else:
                    st.append(int(new_number_str) * current_sign)
                    current_sign = 1

            elif ch in ('*', '/'):
                st.append(ch)
            elif ch == '+':
                current_sign = 1
            elif ch == '-':
                current_sign = -1
            elif ch == '(':
                if current_sign == -1:
                    st.append('-')
                st.append(ch)
                current_sign = 1
            elif ch == ')':
                partial_result = 0
                while st and st[-1] != '(':
                    partial_result += st.pop()
                st.pop()  # to remove open paranthesis
                if st and st[-1] == '-':
                    st.pop()  # to remove '-'
                    st.append(partial_result * -1)
                elif st and st[-1] in ('*', '/'):
                    operator = st.pop()
                    operand1 = st.pop()
                    operand2 = partial_result
                    ans = apply_operator(operand1, operand2, operator)
                    st.append(ans)
                else:
                    st.append(partial_result)

            i += 1

        return sum(st)











