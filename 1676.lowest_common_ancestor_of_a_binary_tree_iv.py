# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode',
                             nodes: 'List[TreeNode]') -> 'TreeNode':
        def DFS(node):
            if not node:
                return 0
            l = DFS(node.left)
            r = DFS(node.right)

            count = l + r
            if node in bag:
                count += 1
            if count == N and not self.ans:
                self.ans = node
            return count

        bag = set(nodes)
        N = len(nodes)
        DFS(root)
        return self.ans
