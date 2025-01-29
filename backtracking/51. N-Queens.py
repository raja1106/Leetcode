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
            if self.noconflict(slate,i,col):
                slate.append(col)
                self.helper(i+1,n,slate,result)
                slate.pop()


    def noconflict(self,slate,row,col):
        for queenrow in range(row):
            if slate[queenrow] == col:
                return False
            rowdiff = abs(row-queenrow)
            coldiff = abs(col-slate[queenrow])
            if rowdiff == coldiff:
                return False
        return True

from typing import List

class Solution_Optimized_approach:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        self.helper(0, n, [], result, set(), set(), set())
        return self.format_result(result, n)

    def helper(self, row, n, slate, result, cols, diag1, diag2):
        if row == n:
            result.append(slate[:])
            return

        for col in range(n):
            if col in cols or (row + col) in diag1 or (row - col) in diag2:
                continue  # Skip invalid placements

            slate.append(col)
            cols.add(col)
            diag1.add(row + col)
            diag2.add(row - col)

            self.helper(row + 1, n, slate, result, cols, diag1, diag2)

            # Backtrack
            slate.pop()
            cols.remove(col)
            diag1.remove(row + col)
            diag2.remove(row - col)

    def format_result(self, result, n):
        """
        Converts column index-based solutions into a board representation.
        """
        return [["." * col + "Q" + "." * (n - col - 1) for col in solution] for solution in result]



obj=Solution()
print(obj.solveNQueens(4))
"""
[[1, 3, 0, 2], [2, 0, 3, 1]]
[[1, 3, 0, 2], [2, 0, 3, 1]]

"""