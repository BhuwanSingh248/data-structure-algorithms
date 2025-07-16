class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        op = [[1]]
        def check_bound(r,c,i,j):
            if j > i:
                return False
            if c < 0 or r < 0:
                return False
            return True
            
        for i in range(1, numRows):
            temp = [1] * (i + 1)
            for j in range(i):
                row = i - 1
                col = j - 1
                is_valid = check_bound(row, col, i, j)
                if is_valid:
                    temp[j] = op[row][j] + op[row][col]     
            op.append(temp)
        return op
                