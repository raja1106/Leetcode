class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        #create a dictionary last that maps each digit to its last occurrence index in the number.
        digits_indices = {int(digit): i for i, digit in enumerate(digits)}

        for i, digit in enumerate(digits):
            for d in range(9, int(digit), -1):
                if digits_indices.get(d, -1) > i:
                    digits[i], digits[digits_indices[d]] = digits[digits_indices[d]], digits[i]
                    return int(''.join(digits))

        return num


class Solution_Bruteforce:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        count = 0
        for i, ch in enumerate(num_str):
            current_num = int(ch)
            max_num = current_num
            max_index = i
            for j in range(i + 1, len(num_str)):
                if int(num_str[j]) >= max_num:
                    max_num = int(num_str[j])
                    max_index = j
            if max_index != i and num_str[max_index] != num_str[i]:
                count += 1
                num_str[i], num_str[max_index] = num_str[max_index], num_str[i]
                break
        return int(''.join(num_str))


# Example usage:
solution = Solution()
print(solution.maximumSwap(3777))  # Output: 7236
print(solution.maximumSwap(98368))  # Output: 9973
