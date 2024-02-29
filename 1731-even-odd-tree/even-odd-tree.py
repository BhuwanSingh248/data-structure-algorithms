# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        arr = deque([root])
        at = []
        op = []
        arr.appendleft(None)

        while arr:
            cq = arr.pop()
            if not cq:
                op.append(at)
                at = []
                if arr:
                    arr.appendleft(None)
            else:
                at.append(cq.val)
                if cq.left:
                    arr.appendleft(cq.left)
                
                if cq.right:
                    arr.appendleft(cq.right)
        print(op)
        # check_even_index:
        
        for i in range(len(op)):
            for j in range(len(op[i])):

                if j ==  len(op[i]) -1:
                    if i%2 == 0 and not op[i][j] %2:
                        return False
                    if i%2 and op[i][j] %2:
                        return False
                else:
                    curr = op[i][j]
                    nxt =  op[i][j+1] 
                    if i%2 == 0:
                        if curr >= nxt or not curr%2:
                            print("froom even => ", i,j)
                            return False
                    else:
                        if curr <= nxt or curr%2 :
                            print('from odd => ', i,j)
                            return False
        return True