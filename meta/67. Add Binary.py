class Solution:
    def addBinary(self, binary1: str, binary2: str) -> str:
        result_bits = []
        index1 = len(binary1) - 1
        index2 = len(binary2) - 1
        carry = 0

        while index1 >= 0 or index2 >= 0 or carry:
            bit1 = int(binary1[index1]) if index1 >= 0 else 0
            bit2 = int(binary2[index2]) if index2 >= 0 else 0
            sum_bits = bit1 + bit2 + carry
            carry, current_bit = divmod(sum_bits, 2)
            result_bits.append(str(current_bit))
            index1 -= 1
            index2 -= 1

        return ''.join(reversed(result_bits))


from collections import deque


class Solution_deque: # reversal not required
    def addBinary(self, binary1: str, binary2: str) -> str:
        result_bits = deque()
        index1 = len(binary1) - 1
        index2 = len(binary2) - 1
        carry = 0

        while index1 >= 0 or index2 >= 0 or carry:
            bit1 = int(binary1[index1]) if index1 >= 0 else 0
            bit2 = int(binary2[index2]) if index2 >= 0 else 0
            sum_bits = bit1 + bit2 + carry
            carry, current_bit = divmod(sum_bits, 2)
            result_bits.appendleft(str(current_bit))
            index1 -= 1
            index2 -= 1

        return ''.join(result_bits)


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








