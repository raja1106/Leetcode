class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, slate):
            if node.left is None and node.right is None:
                slate.append(str(node.val))
                result.append('->'.join(slate))
                slate.pop()
                return
            slate.append(str(node.val))
            if node.left:
                dfs(node.left, slate)
            if node.right:
                dfs(node.right, slate)
            slate.pop()
            return

        result = []
        dfs(root, [])
        return result

    def binaryTreePaths_anotherway(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, slate):
            if node is None:
                return
            if node.left is None and node.right is None:
                slate.append(str(node.val))
                result.append('->'.join(slate))
                slate.pop()
                return
            slate.append(str(node.val))
            dfs(node.left, slate)
            dfs(node.right, slate)
            slate.pop()
            return

        result = []
        dfs(root, [])
        return result


