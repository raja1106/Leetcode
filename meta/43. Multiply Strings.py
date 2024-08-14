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
