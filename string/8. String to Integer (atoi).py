class Solution_Efficient_Version:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)

        # 1) skip leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0

        # 2) sign
        sign = 1
        if s[i] in ['+', '-']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # 3) parse digits with clamp
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # check overflow BEFORE multiplying by 10
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

class Solution_Initial_version:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]

        if not s:
            return 0

        # collect digits
        digits = []
        i = 0
        while i < len(s) and s[i].isdigit():
            digits.append(s[i])
            i += 1

        if not digits:
            return 0

        num = sign * int("".join(digits))

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        return num