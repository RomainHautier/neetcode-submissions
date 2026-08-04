# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = collections.deque([root])
        out = []

        while q:
            level_size = len(q)
            level = []
            print(level_size)
            for _ in range(level_size):
                
                node = q.popleft()
                level.append(node.val)

                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)


            out.append(level)
        
        return out


        