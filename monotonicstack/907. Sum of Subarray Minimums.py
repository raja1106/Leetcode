class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        # `dp` stores the sum of minimums of all subarrays ending at index `i`
        dp = [0] * len(arr)
        st = []  # Monotonic stack to keep track of indices of minimum elements
        result = 0  # To store the final result

        for i in range(len(arr)):
            # Maintain the monotonic property of the stack
            # Pop elements that are >= the current element
            while st and st[-1][0] >= arr[i]:
                st.pop()

            # If the stack is not empty, calculate the span from the last smaller element
            if st:
                prev_index = st[-1][1]
                span = i - prev_index
                dp[i] = dp[prev_index] + span * arr[i]
            else:
                # If the stack is empty, all elements to the left are greater
                span = i + 1
                dp[i] = span * arr[i]

            # Add current dp[i] to the result
            result = (result + dp[i]) % MOD

            # Push the current index onto the stack
            st.append((arr[i], i))

        return result


class Solution_Another_approach:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * n
        MOD = (10 ** 9) + 7
        total_sum = 0
        st = []
        for i in range(n - 1, -1, -1):
            while st and st[-1][1] >= arr[i]:
                st.pop()
            if st:
                span = st[-1][0] - i
                dp[i] = (span * arr[i]) + dp[st[-1][0]]
            else:
                dp[i] = (n - i) * arr[i]

            st.append((i, arr[i]))
            total_sum = (total_sum + dp[i]) % MOD  # 3 2 4 4+4

        return total_sum


class Solution_Bruteforce:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        total_sum = 0
        mod = (10 ** 9) + 7
        for i in range(len(arr)):
            min_element = arr[i]
            total_sum += min_element
            for j in range(i + 1, len(arr)):
                min_element = min(min_element, arr[j])
                total_sum += min_element

        return total_sum % mod

