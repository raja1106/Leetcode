from typing import List
"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""


class Solution:# TLE exception for 2 edges cases
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:# TODOO Need to review this code
        result = set()
        candidates.sort()
        self.combinationSum2Helper(0,candidates,target,[],result,0)
        return list(result)
    def combinationSum2Helper(self, i, candidates, target, current_combination, result, current_sum):
        if current_sum == target:
            result.add(tuple(current_combination[:]))
            return

        if i == len(candidates):
            return

        if candidates[i] > target:
            return

        #exclude

        self.combinationSum2Helper(i + 1, candidates, target, current_combination, result,current_sum)

        #include
        current_combination.append(candidates[i])
        current_sum += candidates[i]
        self.combinationSum2Helper(i + 1, candidates, target, current_combination, result,current_sum)
        current_sum -= candidates[i]
        current_combination.pop()

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self._find_combinations(0, candidates, target, [], result)
        return result

    def _find_combinations(self, start, candidates, target, current_combination, result):
        if target < 0:
            return
        if target == 0:
            result.append(current_combination[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            current_combination.append(candidates[i])
            self._find_combinations(i + 1, candidates, target - candidates[i], current_combination, result)
            current_combination.pop()

# Example usage:
# sol = Solution()
# print(sol.combinationSum2([10,1,2,7,6,1,5], 8))

























