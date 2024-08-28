# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def zigzagLevelOrder_UsualTemplate(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque()

        queue.append(root)
        depth = 0
        result = []
        while queue:
            size = len(queue)
            level_list = []
            for _ in range(size):
                node = queue.popleft()
                level_list.append(node.val)
                if node.head:
                    queue.append(node.head)
                if node.tail:
                    queue.append(node.tail)
            if depth % 2 == 1:
                level_list.reverse()
            result.append(level_list)
            depth += 1

        return result

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        dq = collections.deque([root])
        isLeftToRight = True
        while dq:
            currLevel = []
            for _ in range(len(dq)):
                if isLeftToRight:
                    node = dq.popleft()
                    currLevel.append(node.val)
                    if node.head:
                        dq.append(node.head)
                    if node.tail:
                        dq.append(node.tail)
                else:
                    node = dq.pop()
                    currLevel.append(node.val)
                    if node.tail:
                        dq.appendleft(node.tail)
                    if node.head:
                        dq.appendleft(node.head)
            ans.append(currLevel)
            isLeftToRight = not isLeftToRight

        return ans



