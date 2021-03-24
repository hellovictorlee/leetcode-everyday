# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def DFS(node):
            if not node:
                return None
            l = DFS(node.left)
            r = DFS(node.right)
            if l in (p, q) and r in (p, q):
                self.ans = node
                return None
            if node in (p, q) and (l in (p, q) or r in (p, q)):
                self.ans = node
                return None

            if node in (p, q):
                return node
            if l in (p, q):
                return l
            if r in (p, q):
                return r
            return None

        DFS(root)
        return self.ans
