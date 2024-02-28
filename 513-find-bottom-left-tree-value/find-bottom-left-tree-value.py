# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        maxDepth = [0]

        currDepth = 1
        def dfs(root, currDepth):
            if not root:
                return None
            
            if currDepth > maxDepth[0]:
                ans[0] = root.val
                maxDepth[0] = currDepth
            
            leftLeft = dfs(root.left, currDepth + 1)
            rightLeft = dfs(root.right, currDepth + 1)
        
        dfs(root, currDepth)
        return ans[0]