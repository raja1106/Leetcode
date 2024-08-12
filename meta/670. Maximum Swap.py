class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        digits_indices = {int(digit): i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if digits_indices.get(d, -1) > i:
                    digits[i], digits[digits_indices[d]] = digits[digits_indices[d]], digits[i]
                    return int(''.join(digits))

        return num


# Example usage:
solution = Solution()
print(solution.maximumSwap(3777))  # Output: 7236
print(solution.maximumSwap(98368))  # Output: 9973
