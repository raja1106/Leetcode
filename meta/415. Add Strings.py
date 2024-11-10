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
