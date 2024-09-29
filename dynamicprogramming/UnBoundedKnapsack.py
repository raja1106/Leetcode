def unboundedKnapsack(profits, weights, capacity):
    # Initialize the dp array where dp[i] represents the maximum profit for capacity i
    dp = [0] * (capacity + 1)

    # Iterate over each capacity from 1 to the knapsack capacity
    for c in range(1, capacity + 1):
        max_profit = 0
        # Try every item and check if we can include it
        for i in range(len(profits)):
            if weights[i] <= c:
                # Include the item, and add the profit of the remaining capacity
                max_profit = max(max_profit, profits[i] + dp[c - weights[i]])
        dp[c] = max_profit

    return dp[capacity]

#c --> 0,   15,  (15+15, 150+0) 150, (15+150, 150+15,50+0) 165, (15+165,150+150,50+15,60+0) 300,
# (15+300 150+165,50+150,60+15,290+0) 315,
# (15+315, 150+300,50+165,60+150,290+15 ) 450

# Example usage
profits =[15, 150, 50, 60, 290]
weights = [1, 2, 3, 4, 5]
capacity = 6

print(unboundedKnapsack(profits, weights, capacity))

def unboundedKnapsack_top_down_1(profits, weights, capacity):
    # Initialize a memoization table
    memo = [-1] * (capacity + 1)

    def dfs(current_capacity):
        # Base case: If capacity is 0, profit is 0
        if current_capacity == 0:
            return 0

        # If we have already computed the result for this capacity, return it
        if memo[current_capacity] != -1:
            return memo[current_capacity]

        max_profit = 0
        # Try every item and check if we can include it
        for i in range(len(profits)):
            if weights[i] <= current_capacity:
                # Recursively calculate the profit by including the current item
                profit = profits[i] + dfs(current_capacity - weights[i])
                max_profit = max(max_profit, profit)

        # Store the result in the memoization table
        memo[current_capacity] = max_profit
        return max_profit

    # Start the recursion from the full capacity
    return dfs(capacity)



def unboundedKnapsack_top_down(profits, weights, capacity):
    # Initialize a memoization table
    memo = [-1] * (capacity + 1)

    def dfs(current_capacity):
        # Base case: If capacity exceeds the allowed limit, return 0
        if current_capacity > capacity:
            return 0

        # If we have already computed the result for this capacity, return it
        if memo[current_capacity] != -1:
            return memo[current_capacity]

        max_profit = 0
        # Try every item and check if we can include it
        for i in range(len(profits)):
            if current_capacity + weights[i] <= capacity:
                # Recursively calculate the profit by including the current item
                profit = profits[i] + dfs(current_capacity + weights[i])
                max_profit = max(max_profit, profit)

        # Store the result in the memoization table
        memo[current_capacity] = max_profit
        return max_profit

    # Start the recursion from capacity 0
    dfs(0)
    return memo[capacity]

