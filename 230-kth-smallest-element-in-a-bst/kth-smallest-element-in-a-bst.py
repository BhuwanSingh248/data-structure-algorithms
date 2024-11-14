# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def solve(root, i, k):
            if root == None:
                return -1
            
            left = solve(root.left, i, k)
            if left != -1:
                return left
            i[0]+=1
            if i[0] == k:
                return root.val
            
            return solve(root.right, i, k)

        return solve(root, [0], k)
        