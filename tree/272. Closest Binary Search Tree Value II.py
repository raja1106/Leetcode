class Solution_Best:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        res = collections.deque()

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if len(res) < k:
                res.append(node.val)
            else:
                # If current node is closer than the leftmost element in our window
                if abs(node.val - target) < abs(res[0] - target):
                    res.popleft()
                    res.append(node.val)
                else:
                    # Since it's a BST, if this one is farther, all following are farther
                    return

            inorder(node.right)

        inorder(root)
        return list(res)


import heapq


class Solution_using_max_heap:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        # Heap will store tuples: (-distance, value)
        max_heap = []

        def dfs(node):
            if not node:
                return

            # 1. Calculate distance
            dist = abs(node.val - target)

            # 2. Push to heap (negative dist makes it a max-heap)
            heapq.heappush_max(max_heap, (dist, node.val))

            # 3. If heap size > k, remove the element with the largest distance
            if len(max_heap) > k:
                heapq.heappop_max(max_heap)

            # 4. Continue traversal
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        # Extract values from the heap
        return [val for dist, val in max_heap]