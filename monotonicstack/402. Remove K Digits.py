class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            # Remove digits from the stack if they are bigger than the current digit
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        # If we still have digits to remove, remove from the end
        while k > 0:
            stack.pop()
            k -= 1

        # Convert to string and remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
