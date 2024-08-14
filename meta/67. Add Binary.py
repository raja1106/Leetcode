class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        m = len(a) - 1
        n = len(b) - 1
        result = []

        while m >= 0 or n >= 0 or carry_over:
            op1 = int(a[m]) if m >= 0 else 0
            op2 = int(b[n]) if n >= 0 else 0

            # Compute the sum of two bits plus the carry
            total = op1 + op2 + carry_over

            # Append the current bit to the result
            result.append(str(total % 2))

            # Update carry_over (either 0 or 1)
            carry_over = total // 2

            m -= 1
            n -= 1

        # Since we added digits from the end, reverse the result
        result.reverse()

        return ''.join(result)


class Solution_Naive_Approach:
    def addBinary(self, a: str, b: str) -> str:
        carry_over = 0
        m = len(a) - 1
        n = len(b) - 1
        result = []
        while m >= 0 or n >= 0 or carry_over:
            op1 = int(a[m]) if m >= 0 else 0
            op2 = int(b[n]) if n >= 0 else 0
            if op1 and op2:
                if carry_over:
                    result.append('1')
                else:
                    result.append('0')
                carry_over = 1
            elif op1 or op2:
                if carry_over:
                    result.append('0')
                    carry_over = 1
                else:
                    result.append('1')
                    carry_over = 0
            elif carry_over:
                result.append('1')
                carry_over = 0
            m -= 1
            n -= 1
        result.reverse()
        return ''.join(result)








