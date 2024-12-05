def min_subset_sum_difference(arr):
    total_sum = sum(arr)
    n = len(arr)

    def helper(index, subset_sum):
        if index == n:
            # Calculate the other subset's sum and return the absolute difference
            other_subset_sum = total_sum - subset_sum
            return abs(subset_sum - other_subset_sum)

        # Option 1: Include arr[index] in the subset
        include = helper(index + 1, subset_sum + arr[index])

        # Option 2: Exclude arr[index] from the subset
        exclude = helper(index + 1, subset_sum)

        # Return the minimum difference
        return min(include, exclude)

    return helper(0, 0)


def min_subset_sum_difference(arr):
    total_sum = sum(arr)
    n = len(arr)
    memo = {}

    def helper(index, subset_sum):
        # Base Case
        if index == n:
            other_subset_sum = total_sum - subset_sum
            return abs(subset_sum - other_subset_sum)

        # Check if already computed
        if (index, subset_sum) in memo:
            return memo[(index, subset_sum)]

        # Option 1: Include arr[index] in the subset
        include = helper(index + 1, subset_sum + arr[index])

        # Option 2: Exclude arr[index] from the subset
        exclude = helper(index + 1, subset_sum)

        # Store and return the result
        memo[(index, subset_sum)] = min(include, exclude)
        return memo[(index, subset_sum)]

    return helper(0, 0)
