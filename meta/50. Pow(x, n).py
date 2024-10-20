class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to compute power recursively without using `**`
        def power(base, exp):
            if exp == 0:
                return 1
            half = power(base, exp // 2)  # Recursively compute half power
            result = half * half  # Square the half result

            if exp % 2 != 0:  # If exponent is odd, multiply once more by base
                result *= base

            return result

        # Handle negative exponent by inverting the result
        if n < 0:
            x = 1 / x
            n = -n

        return power(x, n)
