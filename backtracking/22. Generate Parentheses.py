from typing import List
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        self.generateParenthesisHelper(0,0,n,[],result)
        return result

    def generateParenthesisHelper(self,open_parenthesis,closed_parenthesis,n,slate,result):

        if open_parenthesis == closed_parenthesis == n:
            result.append(''.join(slate))
            return

        if open_parenthesis < closed_parenthesis or open_parenthesis > n:
            return

        slate.append('(')
        self.generateParenthesisHelper(open_parenthesis+1, closed_parenthesis, n, slate, result)
        slate.pop()

        slate.append(')')
        self.generateParenthesisHelper(open_parenthesis, closed_parenthesis+1, n, slate, result)
        slate.pop()


