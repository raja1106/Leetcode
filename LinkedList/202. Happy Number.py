class Solution:
    def isHappy(self, n: int) -> bool:
        # 1. Helper function definition
        def get_next_number(x):
            total_sum = 0  # O(1): Initializing a variable is constant time.
            # 2. Loop to sum the squares of digits
            while x:  # The loop runs once per digit in x.
                x, digit = divmod(x, 10)  # O(1) per iteration: divmod operates in constant time.
                total_sum += digit * digit  # O(1) per iteration: multiplication and addition are constant.
            return total_sum  # O(1): Returning the result.
            # Overall for get_next_number(x): It runs in O(d) time where d is the number of digits in x.
            # Since d ≈ log₁₀(x), we can also say it runs in O(log(x)) time.

        # 3. Initialization of pointers for cycle detection
        slow = n  # O(1): Simple assignment.
        fast = get_next_number(n)  # O(log(n)): Computes next number based on n's digits.

        # 4. Cycle detection loop using Floyd's algorithm
        while slow != fast:  # The loop continues until a cycle is detected.
            slow = get_next_number(slow)  # O(log(slow)): Moves one step.
            # For the fast pointer, two steps are taken:
            fast = get_next_number(get_next_number(fast))
            # Each call to get_next_number is O(log(x)). However, note that after the first iteration,
            # the values of slow and fast quickly become much smaller (bounded by a constant, since the maximum
            # sum of squares for any number reduces the magnitude significantly). Thus, after the first few iterations,
            # these calls effectively run in constant time.

        # 5. Return the result based on the meeting point
        return slow == 1  # O(1): A simple comparison.

class Solution_Without_div_mod:
    def isHappy(self, n: int) -> bool:
        def sum_of_digit_squares(number: int) -> int:
            total = 0
            while number:
                digit = number % 10
                total += digit * digit
                number //= 10
            return total

        slow_pointer = n
        fast_pointer = n

        while True:
            slow_pointer = sum_of_digit_squares(slow_pointer)
            fast_pointer = sum_of_digit_squares(sum_of_digit_squares(fast_pointer))
            if slow_pointer == 1 or fast_pointer == 1:
                return True
            if slow_pointer == fast_pointer:
                return False
