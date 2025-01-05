from typing import List

"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
"""

class Solution_Option1:  #combinationSumHelper with Explicit Inclusive/Exclusive Branches
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # Inner helper function
        def combinationSumHelper(i, slate, current_sum):
            if current_sum == target:
                result.append(list(slate))
                return
            if current_sum > target or i == len(candidates):
                return

            # EXCLUSIVE CASE: Skip the candidate at index i
            combinationSumHelper(i + 1, slate, current_sum)

            # INCLUSIVE CASE: Use the candidate at index i
            slate.append(candidates[i])
            combinationSumHelper(i, slate, current_sum + candidates[i]) # here i instead of (i+1) in usual template
            slate.pop()

        combinationSumHelper(0, [], 0)

        return result

class Solution_option_2: #helper with a Loop for Recursive Branches
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
            [2,3,6,7] target =7

        2                   3    6     7

    2  3  6  7 --> for 6,7 here backtracked


        """

        result = []

        def helper(i, current_sum, slate):
            if current_sum == target:
                result.append(list(slate))
                return
            if current_sum > target or i == len(candidates):
                return

            # Recursive case using a loop
            for j in range(i, len(candidates)):
                slate.append(candidates[j])
                helper(j, current_sum + candidates[j], slate)
                slate.pop()

        helper(0, 0, [])
        return result


"""
Time Complexity
The time complexity of the given code primarily depends on the number of potential combinations that can be formed with the given candidates array that sum up to the target. Considering the array has a length n and the recursion involves iterating over candidates and including/excluding them, we get a recursion tree with a depth that could potentially go up to target/min(candidates), if we keep using the smallest element. This leads to an exponential number of possibilities. Thus, the time complexity of the algorithm is O(2^n) in the worst case, when the recursion tree is fully developed. However, since we often return early when s < candidates[i], this is an upper bound.

Space Complexity
The space complexity of the algorithm is also important to consider. It is mainly used by recursion stack space and the space to store combinations. The maximum depth of the recursion could be target/min(candidates) which would at most be O(target) if 1 is in the candidates. However, the space required for the list t, which is used to store the current combination, is also dependent on the target and could at most have target elements when 1 is in the candidates. The space for ans depends on the number of combinations found. Since it's hard to give an exact number without knowing the specifics of candidates and target, we consider it for the upper bound space complexity. Thus, as the list ans grows with each combination found, in the worst case, it could store a combination for every possible subset of candidates, leading to a space complexity of O(2^n * target), where 2^n is the number of combinations and target is the maximum size of any combination.

However, if we look at the auxiliary space excluding the space taken by the output (which is the space ans takes), then the space complexity is O(target) due to the depth of the recursive call stack and the temporary list t.
"""
