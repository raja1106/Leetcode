class Solution:
    def multiply(self, mat1: list[list[int]], mat2: list[list[int]]) -> list[list[int]]:
        rows_mat1 = len(mat1)
        shared_dim = len(mat2)
        cols_mat2 = len(mat2[0])

        result = [[0] * cols_mat2 for _ in range(rows_mat1)]

        for i in range(rows_mat1):               # Iterate over rows of mat1
            for j in range(cols_mat2):           # Iterate over cols of mat2
                for k in range(shared_dim):      # Shared dimension
                    result[i][j] += mat1[i][k] * mat2[k][j]

        return result


from collections import defaultdict
from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, p = len(mat1), len(mat1[0]), len(mat2[0])

        # Step 1: Store non-zero values from mat1
        mat1_map = defaultdict(dict)
        for i in range(m):
            for k in range(n):
                if mat1[i][k] != 0:
                    mat1_map[i][k] = mat1[i][k]

        # Step 2: Store non-zero values from mat2
        mat2_map = defaultdict(dict)
        for k in range(n):
            for j in range(p):
                if mat2[k][j] != 0:
                    mat2_map[k][j] = mat2[k][j]

        # Step 3: Multiply only non-zero combinations
        result = [[0] * p for _ in range(m)]
        for i in mat1_map:
            for k in mat1_map[i]:
                if k in mat2_map:
                    for j in mat2_map[k]:
                        result[i][j] += mat1_map[i][k] * mat2_map[k][j]

        return result

from typing import List
from collections import defaultdict

class Solution_As_Tuple:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, n, p = len(mat1), len(mat1[0]), len(mat2[0])

        # Store non-zero entries of mat1 as (i, k) -> val
        mat1_map = {}
        for i in range(m):
            for k in range(n):
                if mat1[i][k] != 0:
                    mat1_map[(i, k)] = mat1[i][k]

        # Store non-zero entries of mat2 as (k, j) -> val
        mat2_map = {}
        for k in range(n):
            for j in range(p):
                if mat2[k][j] != 0:
                    mat2_map[(k, j)] = mat2[k][j]

        # Initialize result matrix
        result = [[0] * p for _ in range(m)]

        # Multiply only non-zero combinations
        for (i, k1), val1 in mat1_map.items():
            for (k2, j), val2 in mat2_map.items():
                if k1 == k2:
                    result[i][j] += val1 * val2

        return result
