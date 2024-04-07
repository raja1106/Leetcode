from typing import List
"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both 
indicate a queen and an empty space, respectively.
"""


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result=[]
        self.helper(0,n,[],result)
        return result


    def helper(self,i,n,slate,result):
        if i == n:
            result.append(slate[:])

        #Intermediate mgr
        for col in range(0,n):
            if self.noconflict(slate,col):
                slate.append(col)
                self.helper(i+1,n,slate,result)
                slate.pop()


    def noconflict(self,slate,col):

        for queenrow in range(len(slate)):
            if slate[queenrow] == col:
                return False

            rowdiff = abs(len(slate)-queenrow)
            coldiff = abs(col-slate[queenrow])
            if rowdiff == coldiff:
                return False
        return True

obj=Solution()
print(obj.solveNQueens(4))