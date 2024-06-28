from typing import List

"""
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result_set=set([])
        nums.sort()
        self.buildSubsets(0, nums, [], result_set)
        return list(result_set)

    def buildSubsets(self, i, nums, current_subset, result_set):

        if i == len(nums):
            #result.append(list(slate))
            result_set.add(tuple(current_subset[:]))
            return
        #exclude case
        self.buildSubsets(i + 1, nums, current_subset, result_set)

        #include case
        current_subset.append(nums[i])
        self.buildSubsets(i + 1, nums, current_subset, result_set)
        del current_subset[-1]
        #current_subset.pop()

"""
Time Complexity:
The time complexity of this algorithm can be analyzed based on the number of recursive calls and the operations performed on each call.

The function dfs is called recursively, at most, once for every element starting from the current index u. In the worst case, this means potentially calling dfs for each subset of nums.

Since nums has n elements, there are 2^n possible subsets including the empty subset.

However, because the list is sorted and the algorithm skips duplicate elements within the same recursive level, the number of recursive calls may be less than 2^n.

The append and pop methods of a list run in O(1) time.

Therefore, the time complexity of the algorithm is essentially bounded by the number of recursive calls and is O(2^n) in the worst case, when all elements are unique.

Space Complexity:
The space complexity is considered based on the space used by the recursion stack and the space needed to store the subsets (ans).

The maximum depth of the recursive call stack is n, which is the length of nums. Each recursive call uses space for local variables, which is O(n) space in the stack at most.

The list ans will eventually contain all subsets, and thus, it will have 2^n elements, considering each subset as an element. However, the total space taken by all subsets combined is also considerable as each of the 2^n subsets could have up to n elements. This effectively adds up to O(n * 2^n) space.

Considering these factors, the space complexity of the code can be defined as O(n * 2^n) because the space used by the algorithm is proportional to the number of subsets generated, and each subset at most can have n elements.
"""