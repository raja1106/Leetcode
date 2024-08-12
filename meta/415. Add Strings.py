class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1) - 1
        n = len(num2) - 1
        result = []
        carry = 0
        while m >= 0 or n >= 0 or carry:
            x = int(num1[m]) if m >= 0 else 0
            y = int(num2[n]) if n >= 0 else 0
            local_sum = x + y + carry
            carry = local_sum // 10
            result.append(str(local_sum % 10))
            m -= 1
            n -= 1

        return ''.join(result[::-1])

