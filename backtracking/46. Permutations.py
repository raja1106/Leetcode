from typing import List
"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result =[]

        if nums is None or len(nums) == 0:
            return ans

        self.buildPermutations(0,nums,[],result)
        return result

    def buildPermutations(self,i,nums,current_permutation,result):

        def swap(x,y):
            nums[x],nums[y] = nums[y],nums[x]

        if i == len(nums):
            result.append(current_permutation[:])
            return

        for j in range(i,len(nums)):
            current_permutation.append(nums[j])
            swap(j,i)
            self.buildPermutations(i+1,nums,current_permutation,result)
            current_permutation.pop()
            swap(j,i)
        return


"""
Time Complexity O(n * n!)



The time complexity of the algorithm is determined by the number of recursive calls made, and the work done in each call. The function dfs is called recursively until it reaches the base case (i == n).

For n distinct elements, there are n! (factorial of n) permutations. At each level of the recursion, we make n choices, then n - 1 for the next level, and so on, which means we are doing n! work as there are that many permutations to generate and for each of them we do O(1) operation. Hence, the time complexity is O(n!).
"""


