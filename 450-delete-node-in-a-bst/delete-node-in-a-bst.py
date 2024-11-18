# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getMin(root):
            while root.left:
                root = root.left
            return root

        
        def helper(root, key = key):
            if not root:
                return None

            if root.val > key:
                root.left = helper(root.left, key)
            elif key > root.val:
                root.right=helper(root.right, key)
            
            else: 
                if not root.left:
                    return root.right
                
                elif not root.right:
                    return root.left

                min_larger_node = getMin(root.right)
                root.val = min_larger_node.val

                root.right = helper(root.right, min_larger_node.val)


            return root
        
        return helper(root)