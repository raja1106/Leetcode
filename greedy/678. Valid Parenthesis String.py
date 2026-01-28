from functools import lru_cache


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)

        @lru_cache(None)
        def dfs(i, balance):  # open = +1, close = -1
            # invalid prefix
            if balance < 0:
                return False

            if i == len(s):
                if balance == 0:
                    return True
                else:
                    return False

            if s[i] == '(':
                return dfs(i + 1, balance + 1)
            if s[i] == ')':
                return dfs(i + 1, balance - 1)

            if s[i] == '*':
                path1 = dfs(i + 1, balance + 1)
                path2 = dfs(i + 1, balance - 1)
                path3 = dfs(i + 1, balance)
                return path1 or path2 or path3

        return dfs(0, 0)


class Solution_Greedy:
    def checkValidString(self, s: str) -> bool:
        c_min = c_max = 0
        for char in s:
            if char == '(':
                c_min += 1
                c_max += 1
            elif char == ')':
                c_min -= 1
                c_max -= 1
            else:  # char == '*'
                c_min -= 1
                c_max += 1

            if c_max < 0: return False  # Too many ')'
            if c_min < 0: c_min = 0  # c_min can't be negative; '*' doesn't HAVE to be ')'

        return c_min == 0