class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ords = {}
        for i in range(len(matrix)):
            ords[i] = (matrix[i][0], matrix[i][-1])
        # print(ords)
        for key, value in ords.items():
            # print(value)
            if target >=value[0] and target <= value[1]:
                return target in matrix[key]
