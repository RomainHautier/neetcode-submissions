# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invert_left_right(root):

    if not root:
        return root
    root.left, root.right = root.right, root.left
    invert_left_right(root.left)
    invert_left_right(root.right)
    return root

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion along each step.
        # for each node, left becomes right and inversely
        return invert_left_right(root)
        