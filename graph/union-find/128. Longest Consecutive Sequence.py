class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
        self.components = size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.components -= 1


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        # Step 1: Map numbers to indices
        num_to_index = {num: idx for idx, num in enumerate(nums)}
        uf = UnionFind(len(nums))

        # Step 2: Union consecutive numbers
        for num in nums:
            if num + 1 in num_to_index:
                uf.union(num_to_index[num], num_to_index[num + 1])

        # Step 3: Find the largest component size
        return max(uf.size)

# Example Usage
solution = Solution()
nums = [100, 4, 200, 1, 3, 2]
print(solution.longestConsecutive(nums))  # Output: 4


class Solution_Algo:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set from the list for O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        # Iterate over each number in the list
        for number in nums:
            # Check if it's the start of a sequence
            if number - 1 not in num_set:
                # Initialize the current number as the possible start of a sequence
                current_num = number
                current_streak = 1

                # Increment the current_num to find the length of the streak
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest_streak with the maximum streak found
                longest_streak = max(longest_streak, current_streak)

        # Return the length of the longest consecutive sequence
        return longest_streak