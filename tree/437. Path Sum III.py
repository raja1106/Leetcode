class Solution:
    def pathSum(self, root: Optional[TreeNode], target_sum: int) -> int:
        def dfs(node, current_sum):
            if node is None:
                return 0
            current_sum += node.val

            # Number of times the (current_sum - target_sum) has occurred so far
            # which indicates a valid path when subtracted from the current_sum
            total_count = path_counts[current_sum - target_sum]

            # Store the current path's sum in the counter
            path_counts[current_sum] += 1

            # Recursively find paths in left and right subtrees
            total_count += dfs(node.left, current_sum)
            total_count += dfs(node.right, current_sum)

            # Once the node is done, remove its sum from the counter
            # to not use it in the parallel subtree calls
            path_counts[current_sum] -= 1

            # Return the number of paths found
            return total_count

        # Initialize a counter to keep track of all path sums
        path_counts = Counter({0: 1})

        # Call the dfs function from the root of the tree
        return dfs(root, 0)

    def pathSumUsingTotalcountOutside(self, root: Optional[TreeNode], targetSum: int) -> int:
        total_count = 0

        def dfs(node, current_sum):
            nonlocal total_count
            if node is None:
                return
            current_sum += node.val

            # Number of times the (current_sum - targetSum) has occurred so far
            # which indicates a valid path when subtracted from the current_sum
            total_count += path_counts[current_sum - targetSum]

            # Store the current path's sum in the counter
            path_counts[current_sum] += 1

            # Recursively find paths in left and right subtrees
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Once the node is done, remove its sum from the counter
            # to not use it in the parallel subtree calls
            path_counts[current_sum] -= 1

            # Return the number of paths found
            return

        # Initialize a counter to keep track of all path sums
        path_counts = Counter({0: 1})

        # Call the dfs function from the root of the tree
        dfs(root, 0)
        return total_count