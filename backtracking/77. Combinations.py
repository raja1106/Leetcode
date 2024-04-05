from typing import List
"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        nums = [i for i in range(1,n+1)]
        self.buildcombination(0,nums,[],result,k)
        return result

    def buildcombination(self,i,nums,current_combination,result,k):

        if len(current_combination) == k:
            result.append(current_combination[:])
            return

        if i >= len(nums):
            return

        self.buildcombination(i + 1, nums, current_combination, result, k)

        current_combination.append(nums[i])
        self.buildcombination(i+1, nums, current_combination, result, k)
        current_combination.pop()

"""
Time Complexity
The time complexity of this algorithm can be determined by considering the number of recursive calls. At each point, the function has the choice to include a number in the combination or to move past it without including it. This results in the algorithm having a binary choice for each of the n numbers, which hints at a O(2^n) time complexity.

However, due to the nature of combinations, the recursive calls early terminate when the length of the temporary list t equals k. Therefore, the time complexity is better approximated by the number of k-combinations of n, which is O(n choose k). Using binomial coefficient, the time complexity can be expressed as O(n! / (k! * (n - k)!)).

Space Complexity
The space complexity includes the space for the output list and the space used by the call stack due to recursion.

Output List: The output list will hold C(n, k) combinations, and each combination is a list of k elements. Therefore, the space needed for the output list is O(n choose k * k).

Recursion Stack: The maximum depth of the recursion is n because in the worst case, the algorithm would go as deep as trying to decide whether to include the last number. Therefore, the space used by the call stack is O(n).

When considering space complexity, it is important to recognize that the complexity depends on the maximum space usage at any time. So, the space complexity of the DFS recursive solution is dominated by the space needed for the output list. Hence, the space complexity is O(n choose k * k).
"""




































