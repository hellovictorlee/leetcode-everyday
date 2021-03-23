# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        """
        1) current node in (p, q) && left or right in (p, q)
            return None
        2) left in (p, q) and right in (p, q)
            return None
        otherwise:
            return p or q or None
        """
        def DFS(node):
            if not node:
                return None
            l = DFS(node.left)
            r = DFS(node.right)

            # find lca
            if node in (p, q) and (l in (p, q) or r in (p, q)):
                self.ans = node
                return None

            # find lca
            if l in (p, q) and r in (p, q):
                self.ans = node
                return None

            # return find p or q
            if l in (p, q):
                return l
            if r in (p, q):
                return r

            # return node if it is p or q
            if node in (p, q):
                return node
            return None

        DFS(root)
        return self.ans
