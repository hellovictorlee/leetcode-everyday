# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = -1

    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        def DFS(node):
            if not node:
                return (-1, 0)
            l, d_l = DFS(node.left)
            r, d_r = DFS(node.right)
            val = node.val

            if l in (p, q) and r in (p, q):
                self.ans = d_l + d_r
                return (-1, 0)  # (node.val, distance)
            if val in (p, q) and l in (p, q):
                self.ans = d_l
                return (-1, 0)
            if val in (p, q) and r in (p, q):
                self.ans = d_r
                return (-1, 0)

            if val in (p, q):
                return (val, 1)
            if l in (p, q):
                return (l, 1 + d_l)
            if r in (p, q):
                return (r, 1 + d_r)

            return (-1, 0)

        if p == q:
            return 0
        DFS(root)
        return self.ans
