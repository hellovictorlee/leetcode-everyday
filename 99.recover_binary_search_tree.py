# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(node, lst):
            if not node:
                return
            inorder(node.left, lst)
            lst.append(node)
            inorder(node.right, lst)

        lst = []
        # put sorted array by inorder
        inorder(root, lst)

        # find swap nodes
        swap_nodes = [None, None]
        flag = True
        for i in range(1, len(lst)):
            prevVal = lst[i - 1].val
            val = lst[i].val
            if prevVal > val:
                if flag:
                    swap_nodes[0] = lst[i - 1]
                    swap_nodes[1] = lst[i]
                    flag = not flag
                else:
                    swap_nodes[1] = lst[i]

        swap_nodes[0].val, swap_nodes[1].val = swap_nodes[1].val, swap_nodes[
            0].val
