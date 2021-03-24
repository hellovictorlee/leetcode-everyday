"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        bag = set()
        while p:
            bag.add(p)
            p = p.parent

        while q:
            if q in bag:
                return q
            q = q.parent
        return None
