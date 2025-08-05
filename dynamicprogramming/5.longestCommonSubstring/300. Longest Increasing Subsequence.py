from typing import List

class Solution_Top_Down:
    def lengthOfLIS(self, nums):
        memo = {}  # Dictionary for memoization

        def dfs(i, previous_index):
            if i == len(nums):
                return 0  # No elements left to include

            if (i, previous_index) in memo:
                return memo[(i, previous_index)]

            # Exclude current number
            option1 = dfs(i + 1, previous_index)

            # Include current number if it forms an increasing sequence
            option2 = 0
            if previous_index == -1 or nums[i] > nums[previous_index]:
                option2 = 1 + dfs(i + 1, i)  # Update previous index

            memo[(i, previous_index)] = max(option1, option2)
            return memo[(i, previous_index)]

        return dfs(0, -1)  # Start with index 0 and previous_index as -1 (no previous element)

class Solution_Bottom_Up_Approach:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n  # dp[i] stores the LIS ending at index i
        maxLength = 1

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            maxLength = max(maxLength, dp[i])

        return maxLength

""" ---------------------------------------------------------------------"""
class Solution_Bruteforce1_0125:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_val = 1

        def dfs(i, current_seq, previous_no):
            nonlocal max_val
            if i == len(nums):
                max_val = max(max_val, current_seq)
                return
            # Exclude
            dfs(i + 1, current_seq, previous_no)
            # include
            if nums[i] > previous_no:
                dfs(i + 1, current_seq + 1, nums[i])

            return

        dfs(0, 0, float('-inf'))
        return max_val


class Solution_Bruteforce2_0125:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, previous_index):
            if i == len(nums):
                return 0  # No elements left to include

            # Exclude the current number
            option1 = dfs(i + 1, previous_index)

            # Include current number if it forms an increasing sequence
            option2 = 0
            if previous_index == -1 or nums[i] > nums[previous_index]:
                option2 = 1 + dfs(i + 1, i)  # Update previous index

            return max(option1, option2)

        return dfs(0, -1)  # Start with index 0 and previous_index as -1 (no previous element)




# Test Case
sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected Output: 4

# Test Cases
sol = Solution()
print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # Expected Output: 4
print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # Expected Output: 4
print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # Expected Output: 1


class Solution_Brute_Force_1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest_length = -1
        def dfs(i,slate):
            nonlocal longest_length
            if i == len(nums):
                if len(slate) > longest_length:
                    longest_length = len(slate)
                return
            #exclude
            dfs(i+1,slate)
            #include
            if (not slate) or (nums[i] > slate[-1]):
                slate.append(nums[i])
                dfs(i+1,slate)
                slate.pop()
        dfs(0,[])
        return longest_length

class Solution_Bruteforce_2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i,slate):
            key = (i,tuple(slate))
            if key in memo:
                return memo[key]
            if i == len(nums):
                return len(slate)
            #exclude
            exclude_ans = dfs(i+1,slate)
            include_ans = 1
            #include
            if (not slate) or (nums[i] > slate[-1]):
                slate.append(nums[i])
                include_ans = dfs(i+1,slate)
                slate.pop()
            memo[key] = max(include_ans,exclude_ans)
            return max(include_ans,exclude_ans)
        return dfs(0,[])