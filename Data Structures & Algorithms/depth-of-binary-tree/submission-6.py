# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def count_depth(node):
    
    if not node:
        return 0
    return 1 + max(count_depth(node.left), count_depth(node.right))   


    ## 1. has both left and right nodes
    ## c = 1 

    # Left
    ## pass the left node 2
    ## has None, returns c

    return max(l,r)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return count_depth(root)