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


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:# TODOO Need to review this code
        result = set()
        candidates.sort()
        self.combinationSum2Helper(0,candidates,target,[],result)
        return list(result)


    def combinationSum2Helper(self, i, candidates, target, current_combination, result):
        if sum(current_combination) == target:
            result.add(tuple(current_combination[:]))
            return

        if i == len(candidates):
            return

        #exclude

        self.combinationSum2Helper(i + 1, candidates, target, current_combination, result)

        #include
        current_combination.append(candidates[i])
        self.combinationSum2Helper(i + 1, candidates, target, current_combination, result)
        current_combination.pop()




























