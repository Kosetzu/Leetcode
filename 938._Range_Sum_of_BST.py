# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans  = 0
    def rangeSum(self, node:TreeNode, L: int, R: int) -> int:
        if node:
            if node.val >= L and node.val <= R:
                self.ans += node.val
            self.rangeSum(node.left, L, R)
            self.rangeSum(node.right, L, R)
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.rangeSum(root, L, R)
        return self.ans