from typing import List
"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result= []
        self.buildSubsets(0, nums, [], result)
        return result

    def buildSubsets(self, i:int, nums:List[int], current_subset: List[int], result: List[List[int]]):

        if i == len(nums):
            #result.append(list(slate))
            result.append(current_subset[:])
            return
        #exclude case
        self.buildSubsets(i + 1, nums, current_subset, result)

        #include case
        current_subset.append(nums[i])
        self.buildSubsets(i + 1, nums, current_subset, result)
        del current_subset[-1]
        #current_subset.pop()
        return

"""
Time Complexity:
Each number has two possibilities: either it is part of a subset or it is not. Thus, for each element in the input list nums, we are making two recursive calls. This results in a binary decision tree with a total of 2^n leaf nodes (where n is the number of elements in nums).

This leads to a total of 2^n function calls. In each call, we deal with O(1) complexity operations (excluding the recursive calls), such as appending an element to the temporary list t or appending the list to ans.

Therefore, the time complexity of the code is O(2^n).

Space Complexity:
For space complexity, we consider two factors: the space used by the recursive call stack and the space used to store the output.

Recursive Call Stack: In the worst case, the maximum depth of the recursive call stack is n (the number of elements in nums), as we make a decision for each element. Hence, the space used by the call stack is O(n).

Output Space: The space used to store all subsets is the dominating factor. Since there are 2^n subsets and each subset can be at most n elements, the output space complexity is O(n * 2^n).

However, it is important to note that in the context of subsets or combinations problems, the space used to store the output is often considered as auxiliary space and not part of the space complexity used for algorithmic analysis. If we only consider the auxiliary space (ignoring the space for the output), the space complexity would be O(n).

Taking both aspects into account, the total space complexity of the code is O(n * 2^n) considering the space for the output, or O(n) if we are only considering auxiliary space.
"""