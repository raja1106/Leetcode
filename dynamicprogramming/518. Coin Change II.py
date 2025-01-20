class Solution_Bruteforce_Way:
    def change(self, amount: int, coins: List[int]) -> int:
        total_count = 0

        def dfs(i, current_amount):
            nonlocal total_count
            if current_amount == amount:
                total_count += 1
                return
            if current_amount > amount or i == len(coins):
                return

            # Exclude current coin
            dfs(i + 1, current_amount)
            # Include current coin (take it again)
            dfs(i, current_amount + coins[i])

        dfs(0, 0)
        return total_count

class Solution_TopDown_Memo:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}  # Memoization dictionary

        def dfs(i, current_amount):
            if current_amount == amount:
                return 1  # Found one valid way
            if current_amount > amount or i == len(coins):
                return 0  # No valid solution

            # If result is already computed, return it
            if (i, current_amount) in memo:
                return memo[(i, current_amount)]

            # Exclude current coin
            exclude_current = dfs(i + 1, current_amount)
            # Include current coin (take it again)
            include_current = dfs(i, current_amount + coins[i])

            memo[(i, current_amount)] = exclude_current + include_current
            return memo[(i, current_amount)]

        return dfs(0, 0)
