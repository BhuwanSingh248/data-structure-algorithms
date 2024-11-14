# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_valid(root:Optional[TreeNode], n:int, x:int) -> bool:
            if root == None:
                return True
            
            if (root.val > n and root.val < x):
                left:bool = is_valid(root.left, n, root.val)
                right:bool = is_valid(root.right, root.val, x)
                return left and right
            else: return False

        return is_valid(root, -sys.maxsize-1, sys.maxsize)
            