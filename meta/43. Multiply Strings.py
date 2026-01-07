class Solution_easier:
    """
    456
    123
    ----
    1368
      2
    """

    def multiply(self, num1: str, num2: str) -> str:
        multiply_arrays = []
        row_count = 0
        for i in range(len(num2) - 1, -1, -1):
            local_array = []
            local_array.extend(['0'] * row_count)
            carry = 0
            digit = 0
            for j in range(len(num1) - 1, -1, -1):
                digit = carry + int(num1[j]) * int(num2[i])
                carry = digit // 10
                digit = digit % 10
                local_array.append(str(digit))
            local_array.append(str(carry))
            local_array.reverse()
            multiply_arrays.append(''.join(local_array))
            row_count += 1

        result = 0

        for arr in multiply_arrays:
            result += int(arr)

        return str(result)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge cases where either num1 or num2 is '0'
        if num1 == '0' or num2 == '0':
            return '0'

        partial_products = []
        offset = 0

        # Perform multiplication digit by digit
        for digit2_index in range(len(num2) - 1, -1, -1):
            current_product = ['0'] * offset
            carry_over = 0
            for digit1_index in range(len(num1) - 1, -1, -1):
                multiplication = carry_over + int(num1[digit1_index]) * int(num2[digit2_index])
                carry_over = multiplication // 10
                current_product.append(str(multiplication % 10))
            if carry_over > 0:
                current_product.append(str(carry_over))
            current_product.reverse()
            partial_products.append(''.join(current_product))
            offset += 1

        # Initialize the final result as "0"
        total_sum = "0"

        # Add all the partial products together
        for partial in partial_products:
            total_sum = str(int(total_sum) + int(partial))

        return total_sum
