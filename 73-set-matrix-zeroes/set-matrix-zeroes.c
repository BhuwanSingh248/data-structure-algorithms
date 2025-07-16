void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int i, j, k = 0;
    int maxSize = matrixSize * matrixColSize[0];
    int arr[maxSize][2];

    // Step 1: Store positions of zeroes
    for (i = 0; i < matrixSize; i++) {
        for (j = 0; j < matrixColSize[0]; j++) {
            if (matrix[i][j] == 0) {
                arr[k][0] = i; // Row index
                arr[k][1] = j; // Column index
                k++;
            }
        }
    }

    // Step 2: Set rows and columns to zero
    for (int idx = 0; idx < k; idx++) {
        int row = arr[idx][0];
        int col = arr[idx][1];

        for (i = 0; i < matrixSize; i++) {
            matrix[i][col] = 0;
        }

        for (j = 0; j < matrixColSize[0]; j++) {
            matrix[row][j] = 0;
        }
    }
}
