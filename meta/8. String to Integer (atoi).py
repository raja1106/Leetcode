class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Strip leading and trailing whitespaces
        s = s.strip()
        if not s:
            return 0

        # Step 2: Determine the sign
        sign = 1
        j = 0

        if s[0] == '-':
            sign = -1
            j = 1
        elif s[0] == '+':
            j = 1

        # Step 3: Process the digits and build the number
        total = 0
        while j < len(s) and s[j].isdigit():
            total = total * 10 + int(s[j])
            j += 1

        # Apply the sign to the total
        total *= sign

        # Step 4: Handle 32-bit signed integer overflow
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if total < INT_MIN:
            return INT_MIN
        elif total > INT_MAX:
            return INT_MAX

        return total


class Solution_Naive_One:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Strip leading and trailing spaces
        if not s:
            return 0

        sign = 1
        j = 0

        # Check for sign
        if s[0] == '-':
            sign = -1
            j = 1
        elif s[0] == '+':
            j = 1

        # Remove leading zeros
        while j < len(s) and s[j] == '0':
            j += 1

        s = s[j:]
        if not s or not s[0].isdigit():
            return 0

        total = 0
        for char in s:
            if char.isdigit():
                total = total * 10 + int(char)
            else:
                break

        total *= sign

        # Handle 32-bit signed integer overflow
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        if total < INT_MIN:
            return INT_MIN
        elif total > INT_MAX:
            return INT_MAX

        return total
